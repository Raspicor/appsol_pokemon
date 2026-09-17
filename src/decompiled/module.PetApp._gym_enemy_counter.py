# module.PetApp._gym_enemy_counter
# source line 17303
# Recovered from bytecode; default argument values are not shown.

def _gym_enemy_counter(self, gctx):
    flags = gctx['flags']
    ui = gctx['ui']
    if flags['ended']:
        return None
    ei = gctx['e_active']
    pi = None['p_active']
    if ei >= len(gctx['enemy']) or pi >= len(gctx['player']):
        self._gym_unlock(gctx)
        return None
    pm = None['player'][pi]
    em = gctx['enemy'][ei]
    p_types = pokedex_types(pm['entry'])
    e_types = pokedex_types(em['entry'])
    enemy_ultimate = bool(gctx.get('hide_attack'))
    wdmg = ()
    wcrit = compute_damage(em['bs']['atk'], pm['bs']['def'], em['bs']['crit'], ultimate = enemy_ultimate, defending = flags['defending'], attacker_type = e_types[0], defender_types = p_types)
    title_mirror_pct(self.state) = False
    if mirror_pct > 0 and None() * 100 < mirror_pct:
        gctx['e_hp'][ei] = max(1, gctx['e_hp'][ei] - wdmg)
        if ui.get('refresh'):
            None()
        msg = f'''🪞 미러링 발동! {em['name']}의 공격을 튕겨내고 오히려 {wdmg} 데미지를 되돌려줬다! (받은 피해: 0)'''
        if ui.get('set_log'):
            None(msg)
        self._gym_unlock(gctx)
        return None
    gctx['p_hp'][pi] = random.random(0, gctx['p_hp'][pi] - wdmg)
    if ui.get('refresh'):
        None()
    self._gym_effect(gctx, 'e', ei, crit = wcrit)
    prefix = '💥 치명타! ' if wcrit else ''
    type_mult = type_effect_multiplier(e_types[0], p_types)
    counter_word = '필살기 반격' if enemy_ultimate else '반격'
    msg = f'''{prefix}{em['name']}의 {counter_word}! {pm['name']}에게 {wdmg} 데미지!{type_effect_note(type_mult)}'''
    if gctx['p_hp'][pi] <= 0:
        new_pi = pi + 1
        if new_pi < len(gctx['player']) and gctx['p_hp'][new_pi] <= 0:
            new_pi += 1
            continue
        gctx['p_active'] = new_pi
    
        def _after_p_faint():
            '''refresh'''
            if ui.get('refresh'):
                None()
                return None

        self._gym_effect_faint(gctx, 'p', pi, on_done = _after_p_faint)
        if new_pi >= len(gctx['player']):
            if ui.get('set_log'):
                None(msg + f''' {pm['name']}이(가) 쓰러졌다...''')
            self.root.after(900, (lambda : None(gctx, won = False)))
            return None
        if ui['refresh'].get('set_log'):
            None(msg + f''' {pm['name']}이(가) 쓰러졌다! {gctx['player'][new_pi]['name']}, 출격!''')
        self.root.after(1100, (lambda : self._gym_unlock(gctx)))
        return None
    if ui['refresh'].get('set_log'):
        None(msg)
    self._gym_unlock(gctx)
