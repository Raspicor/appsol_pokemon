# module.PetApp._update_keyboard_climb
# source line 9108
# Recovered from bytecode; default argument values are not shown.

def _update_keyboard_climb(self, dt, up, down):
    speed = KB_CLIMB_SPEED * self.state.get('speed_mult', 1)
    top_limit = self.screen_top + 40
    floor_y = self._get_floor_y()
    if not up and down:
        self.pos_y = max(top_limit, self.pos_y - speed * dt)
        self.direction = spriteanim.DIR_UP
        if self.behavior_state != 'climb':
            self.behavior_state = 'climb'
            self.play_action('Walk', loop = True)
            return None
        return None
    if not None and up:
        self.pos_y = min(floor_y, self.pos_y + speed * dt)
        self.direction = spriteanim.DIR_DOWN
        if self.behavior_state != 'climb':
            self.behavior_state = 'climb'
            self.play_action('Walk', loop = True)
            return None
        return None
    if None.behavior_state != 'idle':
        self.behavior_state = 'idle'
        self.play_action('Idle', loop = True)
        return None
