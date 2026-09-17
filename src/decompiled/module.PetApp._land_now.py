# module.PetApp._land_now
# source line 11744
# Recovered from bytecode; default argument values are not shown.

def _land_now(self):
    self.behavior_state = 'acting'
    self._fall_vel = 0
    if self._kb_jump_active:
        self._kb_jump_active
    was_single_kb_jump = not (self._kb_double_jumped)
    self._kb_jumps_used = 0
    self._kb_jump_active = False
    self._kb_double_jumped = False
    self.state['last_interact_time'] = None()
    self.record_daily_action()
    if was_single_kb_jump:
        self._finish_to_idle()
        return None
    if not time.time.resolve('land'):
        time.time.resolve('land')
    land_name = 'Hurt'
    wake_name = self.resolve('wake')

    def _after_land():
        if wake_name:
            self.play_action(wake_name, loop = False, on_complete = self._finish_to_idle)
            return None
        None._finish_to_idle()

    self.play_action(land_name, loop = False, on_complete = _after_land)
