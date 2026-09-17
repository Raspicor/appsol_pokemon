# module.PetApp.total_power_pct
# source line 5248
# Recovered from bytecode; default argument values are not shown.

def total_power_pct(self):
    a = self.total_extra_atk_pct()

    try:
        companion_atk_pct = ()
        _def_pct = companion_synergy_bonus(self.state.get('party', []), self.state.get('caught', { }), self.state.get('mega_party', []))
        title_stat_mult(self.state) = perm_atk_bonus_pct(self.state)
        title_def_pct = title_def_bonus_pct(self.state)
        title_hp_pct = title_hp_pct_bonus(self.state)
        combined = (1 + (a + companion_atk_pct) / 100) * (1 + b / 100) * title_stat_mult_v * (1 + title_def_pct / 100) * (1 + title_hp_pct / 100)
        return (combined - 1) * 100
    except Exception:
        companion_atk_pct = 0
        continue
