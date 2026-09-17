# module.PetApp._gym_build_ui._refresh
# source line 17143
# Recovered from bytecode; default argument values are not shown.

def _refresh():
    ei = gctx['e_active']
    pi = gctx['p_active']
    if ei < len(gctx['enemy']):
        em = gctx['enemy'][ei]
        e_name_var.set(f'''{em['name']} Lv.{em['level']}''')
        e_stat_var.set(f'''체력 {max(0, gctx['e_hp'][ei])}/{gctx['e_hp_max'][ei]}   공 {em['bs']['atk']}  방 {em['bs']['def']}  크리 {em['bs']['crit']:.0f}%''')
        e_pb.configure(value = max(0, gctx['e_hp'][ei]), maximum = gctx['e_hp_max'][ei])
    _roster_line(None(gctx['enemy'], gctx['e_hp'], ei))
    if pi < len(gctx['player']):
        pm = gctx['player'][pi]
        tag = ' 💎' if pm.get('mega') else ''
        p_name_var.set(f'''{pm['name']}{tag} Lv.{pm['level']}''')
        p_stat_var.set(f'''체력 {max(0, gctx['p_hp'][pi])}/{gctx['p_hp_max'][pi]}   공 {pm['bs']['atk']}  방 {pm['bs']['def']}  크리 {pm['bs']['crit']:.0f}%''')
        p_pb.configure(value = max(0, gctx['p_hp'][pi]), maximum = gctx['p_hp_max'][pi])
    _roster_line(None(gctx['player'], gctx['p_hp'], pi))
    self._gym_render_sprites(gctx)
