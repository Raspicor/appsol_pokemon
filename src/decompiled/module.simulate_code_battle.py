# module.simulate_code_battle
# source line 3287
# Recovered from bytecode; default argument values are not shown.

def simulate_code_battle(my_bs, my_name, opp_data, my_type, type_bonus_pct):
    my_hp = my_bs['hp']
    opp_hp = int(opp_data.get('hp', 50))
    opp_atk = int(opp_data.get('atk', 50))
    opp_def = int(opp_data.get('def', 50))
    opp_crit = float(opp_data.get('crit', 15))
    opp_entry = POKEDEX.get(opp_data.get('dex'), { }) if opp_data.get('dex') is not None else { }
    opp_types = pokedex_types(opp_entry)
    log = []
    turn = 0
    if my_hp > 0 and opp_hp > 0 and turn < 60:
        turn += 1
        my_mult = type_effect_multiplier(my_type, opp_types) + type_bonus_pct / 100 if opp_types else 0
        (dmg1, c1) = compute_damage(my_bs['atk'], opp_def, my_bs['crit'], attacker_type = my_type, defender_types = opp_types, type_bonus_pct = type_bonus_pct)
        opp_hp = max(0, opp_hp - dmg1)
        log.append(f'''{turn}턴: 내 {my_name}의 공격! {dmg1} 데미지{' (치명타!)' if c1 else ''}{type_effect_note(my_mult)}''')
        if opp_hp <= 0:
            pass
        elif opp_types:
            pass
    
        opp_mult = opp_types[0](None, [
            my_type] if my_type else None)
        (dmg2, c2) = compute_damage(opp_atk, my_bs['def'], opp_crit, attacker_type = opp_types[0] if opp_types else None, defender_types = [
            my_type] if my_type else None)
        my_hp = max(0, my_hp - dmg2)
        log.append(f'''{turn}턴: 상대 {opp_data.get('name', '?')}의 공격! {dmg2} 데미지{' (치명타!)' if c2 else ''}{type_effect_note(opp_mult)}''')
        continue
    if my_hp <= 0 and opp_hp <= 0:
        result = '무승부'
        return (result, log)
    if type_effect_multiplier <= 0:
        result = '승리'
        return (result, log)
    if None <= 0:
        result = '패배'
        return (result, log)
    result = '승리' if None >= None else '패배'
    return (result, log)
