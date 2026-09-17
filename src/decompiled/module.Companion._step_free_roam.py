# module.Companion._step_free_roam
# source line 4346
# Recovered from bytecode; default argument values are not shown.

def _step_free_roam(self, dt_ms):
    now = None()
    if self.free_x is None:
        sw = max(1, self.owner.screen_w)
        spread_x = self.owner.screen_left + (self.slot_index * 137 + 60) % sw
        self.free_x = spread_x
        self.free_y = self.owner._get_floor_y()
        self.free_target_y = self.free_y
        self.direction = self.owner.direction
        self.free_state = 'idle'
        self._free_target_x = self.free_x
        self._free_next_decision_at = random.uniform + None(0, 1)
        self._turn_until = 0
    min_x = self.owner.screen_left + 30
    max_x = self.owner.screen_left + self.owner.screen_w - 30
    if max_x <= min_x:
        max_x = min_x + 1
    min_y = self.owner.screen_top + 30
    max_y = self.owner.screen_top + self.owner.screen_h - 30
    if max_y <= min_y:
        max_y = min_y + 1
    if not isinstance(self.free_x, (int, float)):
        self.free_x = min_x
    if not isinstance(self.free_y, (int, float)):
        self.free_y = min_y
    self.free_x = max(min_x, min(max_x, self.free_x))
    self.free_y = max(min_y, min(max_y, self.free_y))
    if self.free_state == 'fallen':
        if not self.entry.get('react'):
            self.entry.get('react')
            if not self.entry.get('land'):
                self.entry.get('land')
        fall_action = self.entry['idle']
        if self.anim_set.has(fall_action):
            self.action = fall_action
        if now >= self._free_fallen_until:
            self.free_state = 'idle'
            self.action = self.entry['idle']
            self.frame_idx = 0
            self._free_next_decision_at = random.uniform + None(1, 2.5)
        return None
    if (now + 0.3 + (self.slot_index % 5) * 0.5).free_state == 'playing':
        if not self.entry.get('trick'):
            self.entry.get('trick')
            if not self.entry.get('react'):
                self.entry.get('react')
        play_action = self.entry['idle']
        if self.anim_set.has(play_action):
            self.action = play_action
        if now >= self._free_playing_until:
            self.free_state = 'idle'
            self.action = self.entry['idle']
            self.frame_idx = 0
            self._free_next_decision_at = random.uniform + None(1, 2.5)
        return None
    if None >= time.time._free_next_decision_at:
        pass
    if self.free_state == 'walk':
        speed = 40 * (dt_ms / 1000)
        dx = self._free_target_x - self.free_x
        dy = self.free_target_y - self.free_y
        dist = None(dx, dy)
        if dist > 2:
            step_len = min(speed, dist)
            self.free_x = max(min_x, min(max_x, self.free_x + (dx / dist) * step_len))
            self.free_y = max(min_y, min(max_y, self.free_y + (dy / dist) * step_len))
            new_dir = _dir_from_vector(dx, dy)
        if now < self._turn_until:
            turn_action = self.entry.get('react')
            if turn_action and self.anim_set.has(turn_action):
                pass
            elif self.anim_set.has('Walk'):
                pass
        
            self.action = self.entry['idle']
            return None
        self.action = 'Walk' if now if None() < 0.7 else now if new_dir is not None else math.hypot.anim_set.has('Walk') else self.entry['idle']
        return None
    self.action = now if None() < 0.7 else now.entry['idle']
