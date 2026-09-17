# module._save_obf_decode
# source line 915
# Recovered from bytecode; default argument values are not shown.

def _save_obf_decode(text):
    if not text.startswith(_SAVE_OBF_MAGIC):
        return None

    try:
        scrambled = None(text[len(_SAVE_OBF_MAGIC):].encode('ascii'))
        key = _SAVE_OBF_KEY
        raw = (lambda .0: for None in .0:
    i = ()b = Noneb ^ key[i % len(key)])(enumerate(scrambled)())
        return raw.decode('utf-8')
    except Exception:
        return None
