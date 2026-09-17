# module.PetApp.open_game_feed._resolve
# source line 5959
# Recovered from bytecode; default argument values are not shown.

def _resolve(hit):
    if ctx['resolved']:
        return None
    ctx['resolved'] = None
    None()
    if hit:
        pass
    win.after(280, _new_round)
