# module.Companion.on_release
# source line 4206
# Recovered from bytecode; default argument values are not shown.

def on_release(self, event):
    if self.owner.state.get('companion_layout', 'line') != 'free':
        return None
    if None._dragging:
        if not self._img_w:
            self._img_w
        w = 40
        if not self._img_h:
            self._img_h
        h = 40
        left = event.x_root - self._press_widget_x
        top = event.y_root - self._press_widget_y
        self.free_x = left + w / 2
        self.free_y = top + h
        self._dragging = False
        self.free_state = 'idle'
        self._free_next_decision_at = random.uniform + None(1.5, 3)
        return None
