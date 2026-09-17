# module.PetApp.open_game_throw._step
# source line 6403
# Recovered from bytecode; default argument values are not shown.

def _step():
    if ctx['closed']:
        return None
    None.delete('all')
    canvas.create_rectangle(left_x, bar_y - 6, right_x, bar_y + 6, outline = '#999')
    zs = ctx['zone_start']
    canvas.create_rectangle(zs, bar_y - 6, zs + ctx['zone_w'], bar_y + 6, fill = '#8be07a', outline = '')
    canvas.create_oval(ctx['pos'] - 8, bar_y - 8, ctx['pos'] + 8, bar_y + 8, fill = '#e33333', outline = '#900000', width = 2, tags = 'ball')
    if ctx['pos'] >= right_x:
        right_x = None
        ctx['dir'] = -1
    elif ctx['pos'] <= left_x:
        ctx['pos'] = left_x
        ctx['dir'] = 1
    ctx['job'] = win.after(20, _step)
