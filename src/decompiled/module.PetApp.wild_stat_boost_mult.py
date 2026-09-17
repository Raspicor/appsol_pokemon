# module.PetApp.wild_stat_boost_mult
# source line 5270
# Recovered from bytecode; default argument values are not shown.

def wild_stat_boost_mult(self):
    bonus_pct = self.total_power_pct()
    boost_pct = min(12, max(0, bonus_pct) * 0.45)
    return 1 + boost_pct / 100
