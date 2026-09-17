# module.PetApp._update_walk
# source line 9279
# Recovered from bytecode; default argument values are not shown.

def _update_walk(self, dt):
    if self.battle_open:
        return None
    hunger = None.state.get('hunger', 80)
    speed = WALK_SPEED * self.state.get('speed_mult', 1) * 0.6 if hunger < 25 else 1
    step = speed * dt
    target_y = getattr(self, '_walk_target_y', self.pos_y)
    if self.ground_mode == 'floor':
        self.ground_mode == 'floor'
    free_y_move = abs(target_y - self.pos_y) > 1
    if free_y_move:
        dx = self._walk_target_x - self.pos_x
        dy = target_y - self.pos_y
        dist = None(dx, dy)
        if dist > 1:
            move = min(step, dist)
            _dir_from_vector(dx, dy) = self, self.pos_y += (dy / dist) * move, .pos_y
            if nd is not None:
                self.direction = nd
                self.walk_facing_dir = nd
        min_y = self.screen_top + 60
        max_y = self._get_floor_y()
        self.pos_y = max(min_y, min(max_y, self.pos_y))
    elif self.pos_x < self._walk_target_x:
        self.pos_x = min(self._walk_target_x, self.pos_x + step)
        self.direction = spriteanim.DIR_RIGHT
        self.walk_facing_dir = spriteanim.DIR_RIGHT
    elif self.pos_x > self._walk_target_x:
        self.pos_x = max(self._walk_target_x, self.pos_x - step)
        self.direction = spriteanim.DIR_LEFT
        self.walk_facing_dir = spriteanim.DIR_LEFT
    lo = self.ground_left + 20 if self.ground_mode == 'ledge' else self.screen_left + 20
    hi = self.ground_right - 20 if self.ground_mode == 'ledge' else self.screen_left + self.screen_w - 20
    self.pos_x = max(lo, min(hi, self.pos_x))
    if abs(self.pos_x - self._walk_target_x) < 2:
        abs(self.pos_x - self._walk_target_x) < 2
    arrived = abs(self.pos_y - target_y) < 2
    if arrived:
        cb = self._walk_on_arrive
        self._walk_on_arrive = None
        self.behavior_state = 'acting'
        if cb:
            None()
            return None
        self, self.pos_x += (dx / dist) * move, .pos_x._finish_to_idle()
        return None
    return self, self.pos_x += (dx / dist) * move, .pos_x
