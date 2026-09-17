# module.Companion.on_press
# source line 4176
# Recovered from bytecode; default argument values are not shown.

def on_press(self, event):
    if self.owner.state.get('companion_layout', 'line') != 'free':
        return None
    self._press_x_root = None.x_root
    self._press_y_root = event.y_root
    self._press_widget_x = event.x
    self._press_widget_y = event.y
    self._dragging = False
