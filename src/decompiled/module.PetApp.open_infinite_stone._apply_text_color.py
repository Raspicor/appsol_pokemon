# module.PetApp.open_infinite_stone._apply_text_color
# source line 5795
# Recovered from bytecode; default argument values are not shown.

def _apply_text_color():
    if color_var.get() == 'gray':
        dmg_lbl.configure(fg = '#111')
        hit_lbl.configure(fg = '#111')
        return None
    None.configure(fg = '#a03030')
    hit_lbl.configure(fg = '#ff6a00')
