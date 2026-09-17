# module.PetApp.feed
# source line 11803
# Recovered from bytecode; default argument values are not shown.

def feed(self):
    if self.behavior_state in ('held', 'falling') or self.battle_open:
        return None
    self.state['hunger'] = None(100, self.state.get('hunger', 80) + 35)
    self.state['weight'] = min(100, self.state.get('weight', 50) + 3)
    self._do_one_shot('eat')
