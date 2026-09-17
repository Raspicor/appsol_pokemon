# module.PetApp.open_game_feed._step
# source line 5944
# Recovered from bytecode; default argument values are not shown.

def _step(first):
    if ctx['closed']:
        return None
    None.delete('all')
    canvas.create_line(0, floor_y, 300, floor_y, fill = '#bbb', width = 2)
    canvas.create_oval(ctx['item_x'] - ctx['radius'], ctx['item_y'] - ctx['radius'], ctx['item_x'] + ctx['radius'], ctx['item_y'] + ctx['radius'], fill = '#ff5a5a', outline = '#a02020', width = 2, tags = 'item')
    canvas.create_text(ctx['item_x'], ctx['item_y'], text = '🍎', font = ('맑은 고딕', 14))
    if ctx['item_y'] >= floor_y:
        None(False)
        return None
    win.after(30, _step) = None
