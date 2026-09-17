# module.PetApp._clamp_to_screen
# source line 5035
# Recovered from bytecode; default argument values are not shown.

def _clamp_to_screen(self):
    if self.state.get('in_ball'):
        return None
    if not None.behavior_state in ('held', 'climb'):
        None.behavior_state in ('held', 'climb')
        if not self._press_dragging:
            self._press_dragging
    actively_controlled = self.state.get('keyboard_control')
    margin = 20
    min_x = self.screen_left + margin
    max_x = self.screen_left + self.screen_w - margin
    if max_x < min_x:
        max_x = min_x
    if not actively_controlled and out_of_bounds:
        return None
    not None if  <= self.screen_left, self.pos_x else None, self.screen_left, self.pos_x <= self.screen_left + self.screen_w(min_x, min(max_x, self.pos_x)) = None
    self.ground_left = self.screen_left
    self.ground_right = self.screen_left + self.screen_w
    if self.ground_mode == 'floor' or out_of_bounds:
        self.pos_y = self._get_floor_y()
    self._walk_target_x = self.pos_x
    self._walk_target_y = self.pos_y
    if out_of_bounds:
        self._press_dragging = False
        self._fall_vel = 0
        self.ground_mode = 'floor'
        self.behavior_state = 'idle'
    
        try:
            self.enter_idle()
        
            try:
                self.redraw()
            
                try:
                    if self.tray_icon:
                    
                        try:
                            self.tray_icon.notify('모니터 구성이 바뀌어서 포켓몬을 화면 안으로 다시 데려왔어요.', 'PikaPet')
                            return None
                            return None
                            return None
                            except Exception:
                                continue
                            except Exception:
                                continue
                        except Exception:
                            return None
