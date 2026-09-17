# module.PetApp.set_single_monitor_mode
# source line 4988
# Recovered from bytecode; default argument values are not shown.

def set_single_monitor_mode(self, on):
    self.state['single_monitor_mode'] = bool(on)
    if on:
        self.state['secondary_monitor_mode'] = False
    self.save_state()
    self._refresh_screen_bounds(force = True)
    left = ()
    top = (self.screen_left, self.screen_top, self.screen_w, self.screen_h)
    w = None
    h = None
    if  <= left, self.pos_x or left, self.pos_x <= left + w:
        pass

    if not  <= top, self.pos_y or top, self.pos_y <= top + h:
        pass

    self.force_recall_primary_center()
    return None
