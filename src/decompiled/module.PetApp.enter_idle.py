# module.PetApp.enter_idle
# source line 9041
# Recovered from bytecode; default argument values are not shown.

def enter_idle(self):
    self.behavior_state = 'idle'
    self.play_action('Idle', loop = True)
    self.idle_next_decision_at = random.uniform + None(3, 8)
