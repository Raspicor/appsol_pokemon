# module.PetApp.on_motion
# source line 11669
# Recovered from bytecode; default argument values are not shown.

def on_motion(self, event):
    if self.state.get('in_ball') or self.battle_open:
        return None
    if None.state.get('keyboard_control') and self._kb_jump_active:
        return None
    dx = None.x_root - self._press_x_root
    dy = event.y_root - self._press_y_root
    if not self._press_dragging:
        if abs(dx) < DRAG_THRESHOLD_PX and abs(dy) < DRAG_THRESHOLD_PX:
            return None
        self._press_dragging = None
        self._corner_sleep = False
        self.behavior_state = 'held'
        self.play_action('Idle', loop = True)
    new_left = event.x_root - self._press_widget_x
    new_top = event.y_root - self._press_widget_y

    try:
        self.root.geometry(f'''+{int(new_left)}+{int(new_top)}''')
        return None
    except Exception:
        return None
