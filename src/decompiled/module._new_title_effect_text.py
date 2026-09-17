# module._new_title_effect_text
# source line 2423
# Recovered from bytecode; default argument values are not shown.

def _new_title_effect_text(entry):
    labels = {
        'mine_reward_pct': '광산 플레이당 금액',
        'gold_catch_mult_pct': '야생 포켓몬 승리 시 골드 획득량',
        'gold_mult_pct': '골드 획득량',
        'stone_dmg_pct': '무한의돌 데미지',
        'rocket_crit_pct': '(로켓단 전용) 크리티컬확률',
        'rocket_atk_pct': '로켓단 전용 전투 데미지',
        'ultimate_dmg_pct': '필살기 데미지',
        'hp_pct': 'HP',
        'stat_mult_pct': '총 스탯(HP·공·방)',
        'crit_pct': '크리티컬 확률',
        'def_pct': '방어력',
        'atk_pct': '최종공격력' }
    flat_labels = {
        'mine_win_gold_flat': '야생 포켓몬 승리 시 코인',
        'hp_flat': 'HP' }

    def _fmt(d):
        '''+'''
        parts = []
        for None in d.items():
            k = ()
            v = None
            if not v:
                continue
            if k in flat_labels:
                parts.append(f'''{flat_labels[k]}+{v:.0f}''')
                continue
            if k == 'mirror_pct':
                parts.append(f'''{v:.0f}% 확률로 상대방 공격 미러링(반사)''')
                continue
            if not k in labels:
                continue
        if parts:
            return ', '.join(parts)

    possess_txt = None(entry.get('possess', { }))
    equip = entry.get('equip')
    if entry['id'] == 'shiny_hunter':
        possess_txt = '이로치 조우 확률 1.5배(소폭 상승)'
        equip_txt = '이로치 조우 확률 추가로 4배 (보유효과와 곱해져서 총 6배)'
    elif equip:
        equip_txt = None(equip) + ' (이 칭호를 장착 중일 때만)'
    else:
        equip_txt = '없음 (장착 대상 아님)'
    note = entry.get('note')
    if note:
        return f'''보유효과: {possess_txt}\n장착효과: {equip_txt}''' + f'''\n({note})'''
    return _fmt + f'''보유효과: {possess_txt}\n장착효과: {equip_txt}'''
