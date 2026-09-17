# module.PetApp._do_one_shot
# source line 11784
# Recovered from bytecode; default argument values are not shown.

def _do_one_shot(self, logical, bonus_quota):
    if self.behavior_state in ('held', 'falling') or self.battle_open:
        return None
    action_name = None.resolve(logical)

    def _finish():
        '''idle'''
        self.behavior_state = 'idle'
        self.enter_idle()

    self.state['last_interact_time'] = None()
    if bonus_quota:
        self.record_daily_action()
    self.save_state()
