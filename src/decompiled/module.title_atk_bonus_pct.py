# module.title_atk_bonus_pct
# source line 2022
# Recovered from bytecode; default argument values are not shown.

def title_atk_bonus_pct(state):
    total = 0
    for t in state.get('titles_earned', []):
        tid = t.get('id') if isinstance(t, dict) else t
        if not isinstance(tid, str):
            continue
        if tid in NEW_TITLE_BY_ID:
            continue
        if tid.startswith('inf_stage_'):
            total += TITLE_ATK_BONUS_PCT_INF_STAGE
            continue
        if not is_master_title_id(tid):
            continue
        total += TITLE_MASTER_POSSESS_ATK_PCT
    total += _sum_possess(state, 'atk_pct')
    total += _equip_value(state, 'atk_pct')
    return total
