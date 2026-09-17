# module.PetApp.sleep_now
# source line 11354
# Recovered from bytecode; default argument values are not shown.

def sleep_now(self):
    if self.behavior_state in ('held', 'falling'):
        return None
    None.enter_sleep()
    self.state['last_interact_time'] = None()
    self.record_daily_action()
    self.save_state()
