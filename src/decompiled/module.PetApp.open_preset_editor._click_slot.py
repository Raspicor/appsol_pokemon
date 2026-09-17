# module.PetApp.open_preset_editor._click_slot
# source line 15405
# Recovered from bytecode; default argument values are not shown.

def _click_slot(idx):
    cat = state_box['category']
    if state_box['pending_dex'] is not None:
        pdex = int(state_box['pending_dex'])
        if self._dex_is_taken_by_body(pdex):
            None('PikaPet', '지금 본체(또는 2번 본체)로 쓰고 있는 포켓몬이에요. 이미 그\n능력치를 그대로 받고 있어서, 동료로 또 장착하면 중복이라\n넣을 수 없어요.')
            return None
        existing_slots = None._get_preset_slots(cat)
        if False if any is <common_constant> else (lambda .0: for None in .0:
    i2 = ()s = Noneif not i2 != idx:
    continueif s is not None:
    s is not Noneint(s) == pdex)(enumerate(existing_slots)()):
            None('PikaPet', '이 포켓몬은 이미 이 세팅의 다른 칸에 장착돼 있어요.\n같은 포켓몬을 한 세팅에 두 번 넣을 수는 없어요.')
            return None
        None._set_preset_slot(cat, idx, pdex)
        state_box['pending_dex'] = None
    else:
        slots = self._get_preset_slots(cat)
        if  <= 0, idx or 0, idx < len(slots):
            pass
    
    if slots[idx]:
        self._set_preset_slot(cat, idx, None)
    None()
    None()
