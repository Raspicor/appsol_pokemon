# module.PetApp.exit_ball
# source line 11429
# Recovered from bytecode; default argument values are not shown.

def exit_ball(self):
    self.state['in_ball'] = False
    self.save_state()
    self.behavior_state = 'idle'
    self.enter_idle()
    self.redraw()
    self._apply_body1_visibility()

    try:
        if self.tray_icon:
        
            try:
                self.tray_icon.update_menu()
                return None
                return None
            except Exception:
                return None
