# module.title_effect_text
# source line 2523
# Recovered from bytecode; default argument values are not shown.

def title_effect_text(tid):
    if tid in NEW_TITLE_BY_ID:
        return _new_title_effect_text(NEW_TITLE_BY_ID[tid])
    if None(tid):
        return f'''보유효과: 최종공격력 +{TITLE_MASTER_POSSESS_ATK_PCT:.0f}% (보유 개수만큼 누적)\n장착효과: 총 스탯(HP·공격·방어) +{TITLE_MASTER_EQUIP_STAT_MULT_PCT:.0f}% (마스터 계열 중 하나만 장착 가능)'''
    stat_extra = None
    if tid == 'inf_stage_400':
        stat_extra = f''', 총 스탯(HP·공격·방어) +{TITLE_STAT_MULT_PCT_STAGE400:.0f}%'''
    elif tid == 'inf_stage_800':
        stat_extra = f''', 총 스탯(HP·공격·방어) +{TITLE_STAT_MULT_PCT_STAGE800:.0f}%'''
    return f'''보유효과: 최종공격력 +{TITLE_ATK_BONUS_PCT_INF_STAGE:.0f}%{stat_extra} (그냥 보유만 해도 적용)\n장착효과: 없음 (장착 대상 아님)'''
