# module.PetApp.open_pvp_battle._refresh_opp
# source line 18071
# Recovered from bytecode; default argument values are not shown.

def _refresh_opp():
    if b['opp_hp_max'] is None:
        return None
    None.set(f'''{b['opp_name']} Lv.{b['opp_level']}''')
    opp_stat_var.set(f'''체력 {max(0, b['opp_hp'])}/{b['opp_hp_max']}   공 {b['opp_atk']}  방 {b['opp_def']}  크리 {b['opp_crit']:.0f}%''')
    opp_pb.configure(value = max(0, b['opp_hp']), maximum = b['opp_hp_max'])
