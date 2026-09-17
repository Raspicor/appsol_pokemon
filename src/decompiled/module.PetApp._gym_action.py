# module.PetApp._gym_action
# source line 17197
# Recovered from bytecode; default argument values are not shown.

def _gym_action(self, gctx, kind):
    flags = gctx['flags']
    ui = gctx['ui']
    if flags['locked'] or flags['ended']:
        return None
    ei = gctx['e_active']
    pi = None['p_active']
    if pi >= len(gctx['player']) or ei >= len(gctx['enemy']):
        return None
    flags['locked'] = None
    if ui.get('set_locked'):
        None(True)
    win = gctx['win']
    if kind == 'defend':
        flags['defending'] = True
        if ui.get('set_log'):
            None(f'''{gctx['player'][pi]['name']} 방어 태세! 이번 턴 받는 피해가 줄어들어요.''')
        self.root.after(650, (lambda : self._gym_enemy_counter(gctx)))
        return None
    ultimate = ui['set_locked'] == 'ultimate'
    if ultimate:
        limit = gctx.get('ult_limit', 0)
        repeatable = bool(gctx.get('ult_repeatable'))
        if limit:
            if gctx.get('ult_use_count', 0) >= limit:
                flags['locked'] = False
                if ui.get('set_locked'):
                    None(False)
                if ui.get('set_log'):
                    None(f'''✨ 이번 도전에서 필살기를 이미 {limit}번 다 썼어요.''')
                return None
            gctx['ult_use_count'] = None.get('ult_use_count', 0) + 1
        elif repeatable and pi in gctx['p_ult_used']:
            flags['locked'] = False
            if ui.get('set_locked'):
                None(False)
            return None
        if not repeatable:
            gctx['p_ult_used'].add(pi)
        if ui.get('refresh_ult'):
            None()
    pm = gctx['player'][pi]
    em = gctx['enemy'][ei]
    p_types = pokedex_types(pm['entry'])
    e_types = pokedex_types(em['entry'])
    p_crit = pm['bs']['crit']
    p_atk = pm['bs']['atk']
    if gctx.get('mode') == 'rocket':
        p_atk = int(round(p_atk * (1 + title_rocket_atk_bonus_pct(self.state) / 100)))
        p_crit = p_crit + title_rocket_crit_bonus_pct(self.state)
    ult_bonus_pct = title_ultimate_bonus_pct(self.state) if ultimate else 0
    (dmg, crit) = compute_damage(p_atk, em['bs']['def'], p_crit, ultimate = ultimate, attacker_type = p_types[0], defender_types = e_types, type_bonus_pct = self.companion_type_bonus_pct(e_types) if pm['kind'] == 'body' else 0, ultimate_bonus_pct = ult_bonus_pct)
    gctx['e_hp'][ei] = max(0, gctx['e_hp'][ei] - dmg)
    if ui.get('refresh'):
        None()
    self._gym_effect(gctx, 'p', pi, crit = crit)
    prefix = '💥 치명타! ' if crit else ''
    move_name = pm['entry'].get('ultimate', '필살기') if ultimate else TYPE_SKILL_LABEL.get(p_types[0], '공격')
    type_mult = type_effect_multiplier(p_types[0], e_types)
    if ui.get('set_log'):
        None(f'''{prefix}{pm['name']}의 {move_name}! {em['name']}에게 {dmg} 데미지!{type_effect_note(type_mult)}''')
    if gctx['e_hp'][ei] <= 0:
        new_ei = ei + 1
        if new_ei < len(gctx['enemy']) and gctx['e_hp'][new_ei] <= 0:
            new_ei += 1
            continue
        gctx['e_active'] = new_ei
    
        def _after_e_faint():
            '''refresh'''
            if ui.get('refresh'):
                None()
                return None

        self._gym_effect_faint(gctx, 'e', ei, on_done = _after_e_faint)
        if new_ei >= len(gctx['enemy']):
            self.root.after(900, (lambda : None(gctx, won = True)))
            return None
        if ui['set_log'].get('set_log'):
            None(f'''{em['name']}을(를) 쓰러뜨렸다! 상대가 {gctx['enemy'][new_ei]['name']}을(를) 내보냈다!''')
        self.root.after(1100, (lambda : self._gym_unlock(gctx)))
        return None
    ui['set_log'].root.after(750, (lambda : self._gym_enemy_counter(gctx)))
