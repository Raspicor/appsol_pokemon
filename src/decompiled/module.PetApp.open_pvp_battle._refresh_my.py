# module.PetApp.open_pvp_battle._refresh_my
# source line 18078
# Recovered from bytecode; default argument values are not shown.

def _refresh_my():
    my_pb.configure(value = max(0, b['my_hp']), maximum = b['my_hp_max'])
    my_stat_var.set(f'''체력 {max(0, b['my_hp'])}/{b['my_hp_max']}   공 {b['my_atk']}  방 {b['my_def']}  크리 {b['my_crit']:.0f}%''')
