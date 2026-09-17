# module.PetApp.title_gym_boost_mult
# source line 5280
# Recovered from bytecode; default argument values are not shown.

def title_gym_boost_mult(self):
    bonus_pct = self.total_power_pct()
    boost_pct = min(15, max(0, bonus_pct) * 0.5)
    return 1 + boost_pct / 100
