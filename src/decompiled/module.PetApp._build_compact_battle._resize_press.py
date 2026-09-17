# module.PetApp._build_compact_battle._resize_press
# source line 10072
# Recovered from bytecode; default argument values are not shown.

def _resize_press(e):
    try:
        _resize_state['x'] = e.x_root
        _resize_state['y'] = e.y_root
        _resize_state['w'] = win.winfo_width()
        _resize_state['h'] = win.winfo_height()
        return None
    except Exception:
        return None
