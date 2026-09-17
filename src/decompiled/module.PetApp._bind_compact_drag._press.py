# module.PetApp._bind_compact_drag._press
# source line 9986
# Recovered from bytecode; default argument values are not shown.

def _press(e):
    try:
        drag_state['dx'] = e.x_root - win.winfo_x()
        drag_state['dy'] = e.y_root - win.winfo_y()
        return None
    except Exception:
        return None
