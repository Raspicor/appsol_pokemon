# module.PetApp.open_pvp_battle._do_attack
# source line 18118
# Recovered from bytecode; default argument values are not shown.

def _do_attack():
    if not b['ended'] and b['opp_ready'] or b['my_turn']:
        return None
    dmg = ()
    is_crit = None(b['my_atk'], b['opp_def'], b['my_crit'])
    False = max(0, b['opp_hp'] - dmg)
    None()
    None()
    log_var.set(f'''내가 공격! {dmg} 데미지!''' + ' 💥치명타!' if is_crit else '')

    try:
        client.send({
            'crit': bool(is_crit),
            'dmg': int(dmg),
            'type': 'attack' })
        if b['opp_hp'] <= 0:
            None(True)
            return None
        return _update_atk_btn
    except Exception:
        _refresh_opp
        continue
