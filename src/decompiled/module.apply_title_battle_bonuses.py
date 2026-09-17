# module.apply_title_battle_bonuses
# source line 2070
# Recovered from bytecode; default argument values are not shown.

def apply_title_battle_bonuses(bs, state):
    def_pct = title_def_bonus_pct(state)
    if def_pct:
        bs['def'] = max(1, int(round(bs['def'] * (1 + def_pct / 100))))
    crit_pct = title_crit_bonus_pct(state)
    if crit_pct:
        bs['crit'] = max(5, min(70, bs['crit'] + crit_pct))
    hp_pct = title_hp_pct_bonus(state)
    if hp_pct:
        bs['hp'] = max(1, int(round(bs['hp'] * (1 + hp_pct / 100))))
    hp_flat = title_hp_flat_bonus(state)
    if hp_flat:
        bs['hp'] = max(1, int(round(bs['hp'] + hp_flat)))
    return bs
