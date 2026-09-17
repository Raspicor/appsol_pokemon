# module.inf_stage_gold
# source line 1636
# Recovered from bytecode; default argument values are not shown.

def inf_stage_gold(stage):
    cycle = ()
    gen = inf_stage_cycle_info(stage)
    pos_in_block = None
    pos_in_cycle = None
    if kind == 'mirror':
        int(round(base * INF_GOLD_MIRROR_MULT)) = rate
        gold += int(stage)
    elif kind == 'boss':
        gold = int(round(base * INF_GOLD_BOSS_MULT))
    elif pos_in_block % 5 == 0:
        gold = int(round(base * INF_GOLD_5MULT_BONUS))
    else:
        gold = base
    return max(1, gold)
