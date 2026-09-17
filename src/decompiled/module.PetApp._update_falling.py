# module.PetApp._update_falling
# source line 11714
# Recovered from bytecode; default argument values are not shown.

def _update_falling(self, dt):
    self._fall_vel = min(self._fall_vel + FALL_GRAVITY * dt, FALL_MAX_SPEED)
    new_y = self.pos_y + self._fall_vel * dt
    if not self._check_fall_landing(new_y):
        self.pos_y = new_y
        return None
