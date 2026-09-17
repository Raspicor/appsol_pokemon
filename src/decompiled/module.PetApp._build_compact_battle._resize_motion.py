# module.PetApp._build_compact_battle._resize_motion
# source line 10081
# Recovered from bytecode; default argument values are not shown.

def _resize_motion(e):
    try:
        dx = e.x_root - _resize_state['x']
        dy = e.y_root - _resize_state['y']
        new_w = max(220, _resize_state['w'] + dx)
        new_h = max(200, _resize_state['h'] + dy)
        win.geometry(f'''{new_w}x{new_h}''')
        return None
    except Exception:
        return None
