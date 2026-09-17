# module.PetApp.open_preset_editor._unequip_all
# source line 15259
# Recovered from bytecode; default argument values are not shown.

def _unequip_all():
    cat = state_box['category']
    if not None('PikaPet', f'''{PRESET_CATEGORY_LABEL.get(cat, cat)} 세팅에 장착된 동료를\n전부 해제해서 기존(기본) 세팅으로 되돌릴까요?'''):
        return None
    cap = messagebox.askyesno._preset_cap(cat)
    for i in range(cap):
        self._set_preset_slot(cat, i, None)
    None()
    None()
