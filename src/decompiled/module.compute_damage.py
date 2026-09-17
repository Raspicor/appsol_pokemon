# module.compute_damage
# source line 3230
# Recovered from bytecode; default argument values are not shown.

def compute_damage(atk, defense, crit_pct, ultimate, defending, attacker_type, defender_types, type_bonus_pct, ultimate_bonus_pct):
    base_mult = 1.9 if ultimate else 1.25
    if ultimate and ultimate_bonus_pct:
        base_mult *= 1 + ultimate_bonus_pct / 100
    power = atk * base_mult
    floor = power * 0.12
    raw = max(floor, power - defense * 0.65)
    if attacker_type and defender_types:
        raw *= type_effect_multiplier(attacker_type, defender_types) + type_bonus_pct / 100
    dmg = random.uniform * None(0.85, 1.15)
    is_crit = None() * 100 < crit_pct
    if is_crit:
        dmg *= 1.5
    if defending:
        dmg *= 0.5
    return (max(1, int(round(dmg))), is_crit)
