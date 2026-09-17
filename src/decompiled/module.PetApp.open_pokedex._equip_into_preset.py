# module.PetApp.open_pokedex._equip_into_preset
# source line 16308
# Recovered from bytecode; default argument values are not shown.

def _equip_into_preset(d, category):
    if self._dex_is_taken_by_body(d):
        None('PikaPet', '지금 본체(또는 2번 본체)로 쓰고 있는 포켓몬이에요. 이미 그\n능력치를 그대로 받고 있어서, 동료로 또 장착하면 중복이라\n넣을 수 없어요.')
        return None
    slots = None._get_preset_slots(category)
    if set in (lambda .0: for None in .0:
    x = Noneif x is None:
    continueint(x))(slots()):
        None('PikaPet', '이미 이 상황에 장착돼 있어요.')
        return None
    empty_idx = (lambda .0: for None in .0:
    i = ()s = Noneif s is not None:
    continuei)(enumerate(slots)(), None)
    if empty_idx is None:
        None('PikaPet', f'''{PRESET_CATEGORY_LABEL.get(category, category)}은(는) 지금 {len(slots)}칸이 다 찼어요.\n먼저 아래에서 하나를 해제하고 다시 눌러주세요.''')
        return None
    int(d)._set_preset_slot(category, empty_idx, int(d))
    None()
