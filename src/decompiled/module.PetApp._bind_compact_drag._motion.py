# module.PetApp._bind_compact_drag._motion
# source line 9993
# Recovered from bytecode; default argument values are not shown.

def _motion(e):
    try:
        w = max(80, win.winfo_width())
        h = max(60, win.winfo_height())
        new_x = e.x_root - drag_state['dx']
        new_y = e.y_root - drag_state['dy']
        max_x = self.screen_left + self.screen_w - w
        min_x = self.screen_left
        max_y = self.screen_top + self.screen_h - h
        min_y = self.screen_top
        if max_x < min_x:
            max_x = min_x
        if max_y < min_y:
            max_y = min_y
        new_x = max(min_x, min(max_x, new_x))
        new_y = max(min_y, min(max_y, new_y))
        win.geometry(f'''+{new_x}+{new_y}''')
        return None
    except Exception:
        return None
