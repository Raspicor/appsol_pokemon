# module.PetApp._decay_hunger
# source line 7502
# Recovered from bytecode; default argument values are not shown.

def _decay_hunger(self, dt):
    h = self.state.get('hunger', 80) - dt * 0.0111111
    self.state['hunger'] = max(0, min(100, h))
