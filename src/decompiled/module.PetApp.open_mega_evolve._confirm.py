# module.PetApp.open_mega_evolve._confirm
# source line 12521
# Recovered from bytecode; default argument values are not shown.

def _confirm():
    for None in :
        d = ()
        v = None
        if not v.get():
            continue

    , [], chosen, d = check_vars.items(), d, v
    v = None
    if len(chosen) != MEGA_SACRIFICE_N:
        None('PikaPet', f'''정확히 {MEGA_SACRIFICE_N}마리를 골라주세요.''')
        return None
    if not None('메가진화', f'''고른 {MEGA_SACRIFICE_N}마리를 재물로 바치고 메가진화할까요?\n(도감 기록은 남지만, 더는 장착할 수 없게 돼요)'''):
        return None
    if None.askyesno.mega_has_dual_form():
        form = self._ask_mega_form_choice()
        if form is None:
            return None
        self.state['mega_form'] = None
    ok = ()
    msg = self.do_mega_evolve(chosen)
    None('PikaPet', msg)
    if ok:
        win.destroy()
        return None
    return messagebox.showinfo
