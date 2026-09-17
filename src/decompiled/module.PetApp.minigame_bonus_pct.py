# module.PetApp.minigame_bonus_pct
# source line 5239
# Recovered from bytecode; default argument values are not shown.

def minigame_bonus_pct(self):
    return float(self.state.get('minigame_atk_bonus_pct', 0))
