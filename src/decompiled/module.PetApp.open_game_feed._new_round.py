# module.PetApp.open_game_feed._new_round
# source line 5929
# Recovered from bytecode; default argument values are not shown.

def _new_round():
    if ctx['closed']:
        return None
    if None['round'] >= ctx['rounds']:
        None()
        return None
    None(30, 270) = random.randint
    ctx['item_y'] = 10
    ctx['radius'] = 16 if ctx['round'] > ctx['rounds'] - 3 else 20
    ctx['speed'] = 130 + (ctx['round'] - 1) * 9
    ctx['resolved'] = False
    status_var.set(f'''{ctx['round']}/{ctx['rounds']}라운드  ·  받은 개수 {ctx['hits']}개''')
    None(first = True)
