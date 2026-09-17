# module.PetApp._start_omok_game._place
# source line 6775
# Recovered from bytecode; default argument values are not shown.

def _place(x, y, color):
    ctx['board'][y][x] = color
    margin = ctx['margin']
    cell = ctx['cell']
    px = margin + x * cell
    py = margin + y * cell
    canvas.create_image(px, py, image = ctx['photo'][color], tags = 'stone')
    ctx['last_pos'][color] = (x, y)
    None(color)
