# module.PetApp.train_bonus_pct
# source line 5236
# Recovered from bytecode; default argument values are not shown.

def train_bonus_pct(self):
    return float(self.state.get('train_atk_bonus_pct', 0))
