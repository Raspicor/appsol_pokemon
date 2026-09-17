# module.battle_stats
# source line 2971
# Recovered from bytecode; default argument values are not shown.

def battle_stats(entry, level, atk_pct, def_pct, crit_bonus, extra_atk_pct, own_starter_stage, mega_mult, perm_atk_pct, raised_bonus, perm_all_mult, mega_atk_mult, mega_def_mult):
    eff_atk_mega = mega_atk_mult if mega_atk_mult is not None else mega_mult
    eff_def_mega = mega_def_mult if mega_def_mult is not None else mega_mult
    if own_starter_stage is not None:
        base_mult = starter_level_mult(level, own_starter_stage)
        hp_mult = base_mult * max(0.01, mega_mult)
        atk_mult = base_mult * max(0.01, eff_atk_mega)
        def_mult = base_mult * max(0.01, eff_def_mega)
        hp = max(1, int(round(entry.get('hp', 50) * hp_mult)))
        atk = max(1, int(round(entry.get('atk', 50) * atk_mult)))
        de = max(1, int(round(entry.get('def', 50) * def_mult)))
        if entry.get('legendary'):
            legend_mult = 1 + LEGENDARY_LEVEL_GROWTH_BONUS * (max(1, int(level)) - 1)
            legend_mult *= LEGENDARY_GEN_STAT_MULT.get(legend_gen_for_dex(entry.get('dex', 1)), 1)
            legend_mult *= LEGENDARY_SIGNATURE_TIER_MULT.get(entry.get('dex', 1), 1)
            hp = max(1, int(round(hp * legend_mult)))
            atk = max(1, int(round(atk * legend_mult)))
            de = max(1, int(round(de * legend_mult)))
        else:
            hp = stat_at_level(entry.get('hp', 50), level, reference = STAT_REFERENCE['hp'])
            atk = stat_at_level(entry.get('atk', 50), level, reference = STAT_REFERENCE['atk'])
            de = stat_at_level(entry.get('def', 50), level, reference = STAT_REFERENCE['def'])
            if entry.get('legendary'):
                legend_mult = 1 + LEGENDARY_LEVEL_GROWTH_BONUS * (max(1, int(level)) - 1)
                legend_mult *= LEGENDARY_GEN_STAT_MULT.get(legend_gen_for_dex(entry.get('dex', 1)), 1)
                legend_mult *= LEGENDARY_SIGNATURE_TIER_MULT.get(entry.get('dex', 1), 1)
                hp = max(1, int(round(hp * legend_mult)))
                atk = max(1, int(round(atk * legend_mult)))
                de = max(1, int(round(de * legend_mult)))
            if (mega_mult or mega_mult != 1) and mega_atk_mult is None or mega_def_mult is not None:
                hp = max(1, int(round(hp * max(0.01, mega_mult))))
                atk = max(1, int(round(atk * max(0.01, eff_atk_mega))))
                de = max(1, int(round(de * max(0.01, eff_def_mega))))
    if raised_bonus:
        hp = max(1, int(round(hp * RAISED_STAT_BONUS_MULT)))
        atk = max(1, int(round(atk * RAISED_STAT_BONUS_MULT)))
        de = max(1, int(round(de * RAISED_STAT_BONUS_MULT)))
    atk = int(round(atk * (1 + (atk_pct + extra_atk_pct) / 100)))
    if perm_atk_pct:
        atk = max(1, int(round(atk * (1 + perm_atk_pct / 100))))
    de = int(round(de * (1 + def_pct / 100)))
    if perm_all_mult and perm_all_mult != 1:
        hp = max(1, int(round(hp * perm_all_mult)))
        atk = max(1, int(round(atk * perm_all_mult)))
        de = max(1, int(round(de * perm_all_mult)))
    crit = crit_chance_for(entry) + crit_bonus
    crit = max(5, min(70, crit))
    return {
        'crit': crit,
        'def': de,
        'atk': atk,
        'hp': hp }
