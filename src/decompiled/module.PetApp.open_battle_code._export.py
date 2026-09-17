# module.PetApp.open_battle_code._export
# source line 12789
# Recovered from bytecode; default argument values are not shown.

def _export():
    payload = self._build_battle_code_payload()
    code = encode_battle_code(payload)
    code_entry.delete(0, 'end')
    if not code:
        code
    code_entry.insert(0, '')
    code_entry.select_range(0, 'end')
    code_entry.focus_set()
