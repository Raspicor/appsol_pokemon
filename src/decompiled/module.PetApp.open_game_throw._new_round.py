# module.PetApp.open_game_throw._new_round
# source line 6439
# Recovered from bytecode; default argument values are not shown.

def _new_round():
    if ctx['closed']:
        return None
    if None['round'] >= ctx['rounds']:
        None()
        return None
    max(28, 60 - (ctx['round'] - 1) * 7) = None
    ctx['zone_w'] = zone_w
    ctx['zone_start'] = None(left_x, right_x - zone_w)
    ctx['pos'] = left_x
    ctx['dir'] = 1
    ctx['speed'] = 4 + (ctx['round'] - 1) * 0.4
    ctx['resolved'] = False
    status_var.set(f'''{ctx['round']}/{ctx['rounds']}라운드  ·  성공 {ctx['hits']}개''')
    None()
    None()
