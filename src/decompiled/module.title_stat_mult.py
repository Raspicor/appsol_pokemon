# module.title_stat_mult
# source line 2194
# Recovered from bytecode; default argument values are not shown.

def title_stat_mult(state):
    earned_ids = _earned_ids(state)
    total_pct = 0
    if 'inf_stage_400' in earned_ids:
        total_pct += TITLE_STAT_MULT_PCT_STAGE400
    if 'inf_stage_800' in earned_ids:
        total_pct += TITLE_STAT_MULT_PCT_STAGE800
    total_pct += _sum_possess(state, 'stat_mult_pct')
    equipped = title_equipped_id(state)
    if equipped and is_master_title_id(equipped) and equipped not in NEW_TITLE_BY_ID:
        total_pct += TITLE_MASTER_EQUIP_STAT_MULT_PCT
    else:
        total_pct += _equip_value(state, 'stat_mult_pct')
    return 1 + total_pct / 100
