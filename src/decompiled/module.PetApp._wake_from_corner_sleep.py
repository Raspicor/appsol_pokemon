# module.PetApp._wake_from_corner_sleep
# source line 11557
# Recovered from bytecode; default argument values are not shown.

def _wake_from_corner_sleep(self):
    if self._corner_sleep:
        if self.behavior_state == 'sleep':
            self._corner_sleep = False
            self.behavior_state = 'acting'
            wake_name = self.resolve('wake')
            if wake_name:
                self.play_action(wake_name, loop = False, on_complete = self._finish_to_idle)
                return None
            None._finish_to_idle()
            return None
        return None
