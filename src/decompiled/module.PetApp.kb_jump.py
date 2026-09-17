# module.PetApp.kb_jump
# source line 9145
# Recovered from bytecode; default argument values are not shown.

def kb_jump(self):
    if not self.state.get('keyboard_control'):
        return None
    if None.state.get('in_ball') or self.battle_open:
        return None
    if None.behavior_state == 'falling' and self._kb_jump_active:
        if self._kb_jumps_used < KB_MAX_AIR_JUMPS:
            self._fall_vel = KB_JUMP_VELOCITY_DOUBLE
            True = self, self._kb_jumps_used += 1, ._kb_jumps_used
            self.play_action('Hop', loop = True)
        return None
    if None.behavior_state not in ('idle', 'walk'):
        return None
    self._kb_jumps_used = None
    self._kb_jump_active = True
    self._kb_double_jumped = False
    self._fall_vel = KB_JUMP_VELOCITY_SINGLE
    self.behavior_state = 'falling'
    self.play_action('Hop', loop = True)
