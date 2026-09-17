# module.PetApp._update_sleep
# source line 11362
# Recovered from bytecode; default argument values are not shown.

def _update_sleep(self, now):
    if self._corner_sleep:
        return None
    if None >= None._sleep_until:
        self.state['hunger'] = max(0, self.state.get('hunger', 80) - 3)
        self.behavior_state = 'acting'
        wake_name = self.resolve('wake')
        if wake_name:
            self.play_action(wake_name, loop = False, on_complete = self._finish_to_idle)
            return None
        None._finish_to_idle()
        return None
