# module.PetApp.exercise
# source line 11810
# Recovered from bytecode; default argument values are not shown.

def exercise(self):
    if self.behavior_state in ('held', 'falling') or self.battle_open:
        return None
    self.state['weight'] = None(0, self.state.get('weight', 50) - 4)
    self.state['hunger'] = max(0, self.state.get('hunger', 80) - 6)
    self.behavior_state = 'acting'
    counter = {
        'n': 0 }

    def _hop_chain():
        '''n'''
        if counter['n'] <= 3:
            self.play_action('Hop', loop = False, on_complete = _hop_chain)
            return None
        None() = None.time
        self.record_daily_action()
        self.save_state()
        self._finish_to_idle()

    None()
