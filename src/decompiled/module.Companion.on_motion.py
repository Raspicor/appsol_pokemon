# module.Companion.on_motion
# source line 4186
# Recovered from bytecode; default argument values are not shown.

def on_motion(self, event):
    if self.owner.state.get('companion_layout', 'line') != 'free':
        return None
    if not None(self, '_press_x_root'):
        return None
    dx = None.x_root - self._press_x_root
    dy = event.y_root - self._press_y_root
    if not self._dragging:
        if abs(dx) < DRAG_THRESHOLD_PX and abs(dy) < DRAG_THRESHOLD_PX:
            return None
        self._dragging = None
        self.free_state = 'idle'
        self.action = self.entry['idle'] if self.entry else 'Idle'
    new_left = event.x_root - self._press_widget_x
    new_top = event.y_root - self._press_widget_y

    try:
        self.win.geometry(f'''+{int(new_left)}+{int(new_top)}''')
        return None
    except Exception:
        return None
