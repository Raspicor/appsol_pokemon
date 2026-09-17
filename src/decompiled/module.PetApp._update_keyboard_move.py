# module.PetApp._update_keyboard_move
# source line 9078
# Recovered from bytecode; default argument values are not shown.

def _update_keyboard_move(self, dt):
    if self.state.get('in_ball') or self.battle_open:
        return None
    up = None._key_up
    down = self._key_down
    if up or down:
        self._update_keyboard_climb(dt, up, down)
        return None
    left = None._key_left
    right = self._key_right
    speed = WALK_SPEED * self.state.get('speed_mult', 1) * 1.2
    if not left and right:
        self.pos_x = max(self.screen_left + 40, self.pos_x - speed * dt)
        self.direction = spriteanim.DIR_LEFT
        self.walk_facing_dir = spriteanim.DIR_LEFT
        if self.behavior_state != 'walk':
            self.behavior_state = 'walk'
            self.play_action('Walk', loop = True)
            return None
        return None
    if not None and left:
        self.pos_x = min(self.screen_left + self.screen_w - 40, self.pos_x + speed * dt)
        self.direction = spriteanim.DIR_RIGHT
        self.walk_facing_dir = spriteanim.DIR_RIGHT
        if self.behavior_state != 'walk':
            self.behavior_state = 'walk'
            self.play_action('Walk', loop = True)
            return None
        return None
    if None.behavior_state != 'idle':
        self.behavior_state = 'idle'
        self.play_action('Idle', loop = True)
        return None
