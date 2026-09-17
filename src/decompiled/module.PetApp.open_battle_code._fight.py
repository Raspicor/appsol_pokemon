# module.PetApp.open_battle_code._fight
# source line 12805
# Recovered from bytecode; default argument values are not shown.

def _fight():
    data = decode_battle_code(opp_entry.get())
    if not data:
        None('PikaPet', '코드가 올바르지 않아요. 정확히 복사해서 붙여넣어 주세요.')
        return None
    None.destroy()
    self._open_code_battle_window(data)
