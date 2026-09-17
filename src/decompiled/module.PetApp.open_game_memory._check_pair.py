# module.PetApp.open_game_memory._check_pair
# source line 6115
# Recovered from bytecode; default argument values are not shown.

def _check_pair():
    if ctx['closed']:
        return None
    if None(ctx['revealed']) != 2:
        return None
    (i1, i2) = None['revealed']
    if deck[i1] == deck[i2]:
        ctx['matched'].add(i1)
        ctx['matched'].add(i2)
        ctx['revealed'] = []
        ctx['locked'] = False
        if len(ctx['matched']) == len(deck):
            None()
            return None
        return None
    status_var.set(f'''실수 {ctx['mistakes']}회''')
    (lambda : if ctx['closed']:
    Nonefor idx in (None, i2):
    btn = ctx['buttons'].get(idx)if btn is None:
    continuebtn.configure(image = back_img)ctx['revealed'] = []ctx['locked'] = FalseNoneexcept Exception:
    continue) = None
    win.after(700, _hide_back)
