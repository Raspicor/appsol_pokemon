# module.PetApp.enter_sleep
# source line 11347
# Recovered from bytecode; default argument values are not shown.

def enter_sleep(self):
    self.behavior_state = 'sleep'
    self._corner_sleep = False
    self.play_action('Sleep', loop = True)
    self._sleep_started_at = None()
    self._sleep_until = random.uniform + None(20, 60)
