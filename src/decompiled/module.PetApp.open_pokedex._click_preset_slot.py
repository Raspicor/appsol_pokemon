# module.PetApp.open_pokedex._click_preset_slot
# source line 16420
# Recovered from bytecode; default argument values are not shown.

def _click_preset_slot(category, idx):
    d = selected['dex']
    if d is not None and selected['status'] == 'caught':
        if set in (lambda .0: for x in .0:
    int(x).0)(self.state.get('sacrificed', [])()):
            None('PikaPet', '메가진화 재물로 이미 바친 포켓몬이라 장착할 수 없어요.')
            return None
        if None._dex_is_taken_by_body(d):
            None('PikaPet', '지금 본체(또는 2번 본체)로 쓰고 있는 포켓몬이에요. 이미 그\n능력치를 그대로 받고 있어서, 동료로 또 장착하면 중복이라\n넣을 수 없어요.')
            return None
        existing_slots = int(d)._get_preset_slots(category)
        if False if any is <common_constant> else (lambda .0: for None in .0:
    i2 = ()s = Noneif not i2 != idx:
    continueif s is not None:
    s is not Noneint(s) == int(d))(enumerate(existing_slots)()):
            None('PikaPet', '이 포켓몬은 이미 이 세팅의 다른 칸에 장착돼 있어요.\n같은 포켓몬을 한 세팅에 두 번 넣을 수는 없어요.')
            return None
        None._set_preset_slot(category, idx, int(d))
    else:
        cur_slots = self._get_preset_slots(category)
        if  <= 0, idx or 0, idx < len(cur_slots):
            pass
    
    if cur_slots[idx]:
        self._set_preset_slot(category, idx, None)
    None()
