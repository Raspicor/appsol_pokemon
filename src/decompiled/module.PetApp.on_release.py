# module.PetApp.on_release
# source line 11692
# Recovered from bytecode; default argument values are not shown.

def on_release(self, event):
    if self.state.get('in_ball') or self.battle_open:
        return None
    if None._press_dragging:
    
        try:
            if not self._img_w:
                self._img_w
            w = 60
            if not self._img_h:
            
                try:
                    self._img_h
                    h = 60
                    left = event.x_root - self._press_widget_x
                    top = event.y_root - self._press_widget_y
                    self.pos_x = int(left + w / 2)
                    self.pos_y = int(top + h)
                    self.behavior_state = 'falling'
                    self._fall_vel = 0
                    self._press_dragging = False
                    return None
                    self.tickle()
                    return None
                except Exception:
                
                    try:
                        continue
                    
                        try:
                            pass
                        except:
                            self.behavior_state = 'falling'
                            self._fall_vel = 0
                            self._press_dragging = False
