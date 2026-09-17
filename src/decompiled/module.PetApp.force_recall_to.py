# module.PetApp.force_recall_to
# source line 11443
# Recovered from bytecode; default argument values are not shown.

def force_recall_to(self, x, y):
    if self._hide_timer_id is not None:
    
        try:
            self.root.after_cancel(self._hide_timer_id)
            self._hide_timer_id = None
            was_in_ball = self.state.get('in_ball', False)
            self.state['in_ball'] = False
            self._press_dragging = False
            self._fall_vel = 0
            self.ground_mode = 'floor'
            self.ground_left = self.screen_left
            self.ground_right = self.screen_left + self.screen_w
            margin = 20
            min_x = self.screen_left + margin
            max_x = self.screen_left + self.screen_w - margin
            if max_x < min_x:
                max_x = min_x
            min_y = self.screen_top + margin
            max_y = self.screen_top + self.screen_h - margin
            if max_y < min_y:
                max_y = min_y
            self.pos_x = max(min_x, min(max_x, int(x)))
            self.pos_y = max(min_y, min(max_y, int(y)))
            self.behavior_state = 'idle'
            self.enter_idle()
        
            try:
                self.root.deiconify()
                self.redraw()
                self._apply_body1_visibility()
                self.save_state()
                if was_in_ball:
                
                    try:
                        if self.tray_icon:
                        
                            try:
                                self.tray_icon.update_menu()
                                return None
                                return None
                                return None
                                except Exception:
                                    continue
                                except Exception:
                                    continue
                            except Exception:
                                return None
