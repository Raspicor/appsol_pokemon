# module.PetApp._kb_apply_air_move
# source line 9133
# Recovered from bytecode; default argument values are not shown.

def _kb_apply_air_move(self, dt):
    left = self._key_left
    right = self._key_right
    speed = WALK_SPEED * self.state.get('speed_mult', 1) * KB_AIR_MOVE_MULT
    if not left and right:
        self.pos_x = max(self.screen_left + 40, self.pos_x - speed * dt)
        self.direction = spriteanim.DIR_LEFT
        return None
    if None:
        if not left:
            self.pos_x = min(self.screen_left + self.screen_w - 40, self.pos_x + speed * dt)
            self.direction = spriteanim.DIR_RIGHT
            return None
        return None
