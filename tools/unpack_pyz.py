import struct, marshal, zlib, os
d=open('extracted/PYZ.pyz','rb').read()
(tocpos,) = struct.unpack('!I', d[8:12])
toc = marshal.loads(d[tocpos:])
items = list(toc.items()) if isinstance(toc,dict) else toc
WANT = ('spriteanim','winlayer')
os.makedirs('app_pyz', exist_ok=True)
n=0
for name, (ispkg, pos, length) in items:
    if name.split('.')[0] not in WANT: continue
    blob = zlib.decompress(d[pos:pos+length])
    path = name.replace('.','/')
    path = path + ('/__init__' if ispkg else '')
    dest = os.path.join('app_pyz', path + '.pyc')
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    # rebuild a real 3.14 pyc header: magic(4) + flags(4) + mtime(4) + size(4)
    open(dest,'wb').write(b'\xfa\x0d\x0d\x0a' + b'\0'*12 + blob)
    print(f"  {name:40s} pkg={ispkg} {len(blob):>8} bytes")
    n+=1
print("extracted", n)
