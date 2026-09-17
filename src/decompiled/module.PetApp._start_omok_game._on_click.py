# module.PetApp._start_omok_game._on_click
# source line 6835
# Recovered from bytecode; default argument values are not shown.

def _on_click(event):
    if ctx['locked'] and ctx['game_over'] or ctx['closed']:
        return None
    margin = None['margin']
    cell = ctx['cell']
    if cell <= 0:
        return None
    gx = None((event.x - margin) / cell)
    gy = round((event.y - margin) / cell)
    if  <= 0, gx or 0, gx < n:
        pass
    else:
        return None
    if not  <= None, gy or None, gy < n:
        return None
    return None
    if ctx['board'][gy][gx] is not None:
        return None
    ctx['turn'] = None
    None(gx, gy, color)
    None(gx, gy, color)
