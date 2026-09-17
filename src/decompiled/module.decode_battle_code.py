# module.decode_battle_code
# source line 3273
# Recovered from bytecode; default argument values are not shown.

def decode_battle_code(code):
    try:
        if not code:
        
            try:
                code
                code = ''.strip()
                if not code.startswith(BATTLE_CODE_PREFIX):
                    return None
                raw = None(code[len(BATTLE_CODE_PREFIX):].encode('ascii'))
                data = None(raw.decode('utf-8'))
                if isinstance(data, dict) or 'hp' not in data:
                    return None
                return json.loads
            except Exception:
                return None
