import marshal, os, sys, subprocess, importlib.util, re

PYCDC = os.path.abspath('pycdc/pycdc')
MAGIC = importlib.util.MAGIC_NUMBER
CO_VARARGS, CO_VARKEYWORDS, CO_GENERATOR, CO_COROUTINE = 4, 8, 32, 128

def load(p):
    b = open(p, 'rb').read()
    return marshal.loads(b[16:] if b[:4] == MAGIC else b)

def signature(co):
    """Rebuild a def line from the code object's own metadata.
    Default values live in the *parent* frame, so they can't appear here."""
    n = co.co_argcount + co.co_kwonlyargcount
    names = list(co.co_varnames[:n])
    pos = names[:co.co_argcount]
    kwonly = names[co.co_argcount:n]
    extra = co.co_argcount + co.co_kwonlyargcount
    parts = []
    if co.co_posonlyargcount:
        parts += pos[:co.co_posonlyargcount] + ['/']
        pos = pos[co.co_posonlyargcount:]
    parts += pos
    if co.co_flags & CO_VARARGS:
        parts.append('*' + co.co_varnames[extra]); extra += 1
    elif kwonly:
        parts.append('*')
    parts += kwonly
    if co.co_flags & CO_VARKEYWORDS:
        parts.append('**' + co.co_varnames[extra])
    kind = 'async def' if co.co_flags & CO_COROUTINE else 'def'
    return f"{kind} {co.co_name}({', '.join(parts)}):"

def decompile(co, tmp):
    with open(tmp, 'wb') as f:
        f.write(MAGIC + b'\0' * 12 + marshal.dumps(co))
    r = subprocess.run([PYCDC, tmp], capture_output=True, text=True, timeout=120)
    body = [l for l in r.stdout.split('\n')
            if not l.startswith('# Source Generated') and not l.startswith('# File:')]
    while body and not body[0].strip(): body.pop(0)
    while body and not body[-1].strip(): body.pop()
    return '\n'.join(body), r.stderr

def walk(co, path, out):
    """Yield (qualified_name, code_object, immediate children)."""
    kids = [k for k in co.co_consts if hasattr(k, 'co_name')]
    out.append((path, co, kids))
    for k in kids:
        walk(k, f"{path}.{k.co_name}", out)

if __name__ == '__main__':
    src, dest = sys.argv[1], sys.argv[2]
    co = load(src)
    objs = []
    walk(co, co.co_name if co.co_name != '<module>' else 'module', objs)
    os.makedirs(dest, exist_ok=True)
    tmp = '/tmp/_one.pyc'
    ok = bad = 0
    index = []
    for qual, c, kids in objs:
        if c.co_name in ('<listcomp>','<dictcomp>','<setcomp>','<genexpr>','<lambda>'):
            continue    # inlined into their parent's source already
        text, err = decompile(c, tmp)
        broken = 'WARNING: Decompyle incomplete' in text or not text.strip()
        ok, bad = (ok, bad + 1) if broken else (ok + 1, bad)
        safe = re.sub(r'[^A-Za-z0-9_.-]', '_', qual)[:150]
        head = [f"# {qual}", f"# source line {c.co_firstlineno}",
                "# Recovered from bytecode; default argument values are not shown.",
                ""]
        if c.co_name != '<module>':
            head.append(signature(c))
            text = '\n'.join(('    ' + l if l.strip() else l) for l in text.split('\n'))
        open(os.path.join(dest, safe + '.py'), 'w').write('\n'.join(head) + '\n' + text + '\n')
        index.append((qual, c.co_firstlineno, 'PARTIAL' if broken else 'ok', len(text.split('\n'))))
    print(f"decompiled {ok} clean, {bad} partial, {len(index)} files -> {dest}")
    with open(os.path.join(dest, '_INDEX.txt'), 'w') as f:
        for q, ln, st, n in sorted(index, key=lambda x: x[1]):
            f.write(f"{st:8s} line {ln:>6}  {n:>5} lines  {q}\n")
