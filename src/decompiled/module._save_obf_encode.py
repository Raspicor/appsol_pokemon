# module._save_obf_encode
# source line 907
# Recovered from bytecode; default argument values are not shown.

def _save_obf_encode(json_text):
    raw = json_text.encode('utf-8')
    key = _SAVE_OBF_KEY
    scrambled = (lambda .0: for None in .0:
    i = ()b = Noneb ^ key[i % len(key)])(enumerate(raw)())
    return base64.b64encode + None(scrambled).decode('ascii')
