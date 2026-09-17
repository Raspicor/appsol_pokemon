# module.PetApp.sleep_in_corner
# source line 11524
# Recovered from bytecode; default argument values are not shown.

def sleep_in_corner(self):
    if self.state.get('in_ball') or self.behavior_state in ('held', 'falling'):
        return None
    if None._hide_timer_id is not None:
    
        try:
            self.root.after_cancel(self._hide_timer_id)
            self._hide_timer_id = None
            self._press_dragging = False
            self._fall_vel = 0
            self.ground_mode = 'floor'
            self.ground_left = self.screen_left
            self.ground_right = self.screen_left + self.screen_w
            self.pos_x = self.screen_left + self.screen_w - 50
            self.pos_y = self._get_floor_y()
            self.direction = spriteanim.DIR_LEFT
            self.walk_facing_dir = spriteanim.DIR_LEFT
        
            try:
                self.root.deiconify()
                self.enter_sleep()
                self._corner_sleep = True
                self.state['last_interact_time'] = None()
                self.record_daily_action()
                self.redraw()
                self.save_state()
                return None
                except Exception:
                    continue
            except Exception:
                continue
