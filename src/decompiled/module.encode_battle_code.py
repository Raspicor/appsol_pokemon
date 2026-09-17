# module.encode_battle_code
# source line 3265
# Recovered from bytecode; default argument values are not shown.

def encode_battle_code(payload):
    try:
        raw = None(payload, ensure_ascii = False, separators = (',', ':')).encode('utf-8')
        return base64.urlsafe_b64encode + None(raw).decode('ascii')
    except Exception:
        return None
