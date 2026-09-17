# module.PetApp._weight_factor
# source line 5085
# Recovered from bytecode; default argument values are not shown.

def _weight_factor(self):
    w = self.state.get('weight', 50)
    return 0.9 + 0.2 * (w / 100)
