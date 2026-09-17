# module.PetApp._start_omok_game._draw_last_mark
# source line 6702
# Recovered from bytecode; default argument values are not shown.

def _draw_last_mark(color):
    canvas.delete(f'''lastmark_{color}''')
    pos = ctx['last_pos'].get(color)
    if not pos:
        return None
    xx = ()
    yy = None
    ctx['cell'] = ctx['margin']
    px = margin + xx * cell
    py = margin + yy * cell
    r = max(3, cell * 0.17)
    canvas.create_oval(px - r, py - r, px + r, py + r, outline = '#ff3b30', width = 2, tags = f'''lastmark_{color}''')
