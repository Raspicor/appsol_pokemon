# module.PetApp.open_game_feed._on_click
# source line 5968
# Recovered from bytecode; default argument values are not shown.

def _on_click(evt):
    if ctx['closed'] and ctx['resolved'] or ctx['round'] == 0:
        return None
    dx = None.x - ctx['item_x']
    dy = evt.y - ctx['item_y']
    if (dx * dx + dy * dy) ** 0.5 <= ctx['radius'] + 6:
        None(True)
        return None
