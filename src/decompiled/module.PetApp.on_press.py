# module.PetApp.on_press
# source line 11657
# Recovered from bytecode; default argument values are not shown.

def on_press(self, event):
    self._grab_keyboard_focus()
    if self.state.get('in_ball') or self.battle_open:
        return None
    self._press_x_root = None.x_root
    self._press_y_root = event.y_root
    self._press_widget_x = event.x
    self._press_widget_y = event.y
    self._press_dragging = False
