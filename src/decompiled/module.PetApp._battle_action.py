# module.PetApp._battle_action
# source line 10918
# Recovered from bytecode; default argument values are not shown.

def _battle_action(self, ctx, kind):
    flags = ctx['flags']
    hp = ctx['hp']
    ui = ctx['update_ui']
    if not flags['locked'] and hp['wild'] <= 0 or any_body_alive(ctx):
        return None
    flags['locked'] = None
    if ui.get('set_locked'):
        None(True)
    win = ctx['win']
    if kind == 'flee':
        flags['started'] = True
        if ui.get('set_log'):
            None('도망쳤다...')
        self._finish_battle(ctx, False, entered_fight = True)
        return None
    flags['started'] = ui['set_locked']
    entry = ctx['entry']
    wild_bs = ctx['wild_bs']
    attacker = ctx.get('active', 'player')
    attacker_bs = body_bs(ctx, attacker)
    attacker_entry = body_entry(ctx, attacker)
    attacker_types = pokedex_types(attacker_entry)
    attacker_label = f'''내 {self.display_name()}''' if attacker == 'player' else f'''내 {attacker_entry.get('kr', '2번 본체')}'''
    if kind == 'defend':
        flags['defending'] = True
        if ui.get('set_log'):
            None(f'''{attacker_label} 방어 태세! 이번 턴 받는 피해가 줄어들어요.''')
        win.after(700, (lambda : self._wild_turn(ctx)))
        return None
    ultimate = None == 'ultimate'
    if ultimate:
        if flags['ultimate_used'].get(attacker, False):
            flags['locked'] = False
            if ui.get('set_locked'):
                None(False)
            return None
        flags['ultimate_used'][attacker] = None
        if ui.get('refresh_ult'):
            None()
    (dmg, crit) = compute_damage(attacker_bs['atk'], wild_bs['def'], attacker_bs['crit'], ultimate = ultimate, attacker_type = attacker_types[0], defender_types = pokedex_types(entry), type_bonus_pct = self.companion_type_bonus_pct(pokedex_types(entry)))
    hp['wild'] = max(0, hp['wild'] - dmg)
    if ui.get('refresh_bars'):
        None()
    if ui.get('effect'):
        None(attacker, crit = crit)
    if hp['wild'] <= 0 and ui.get('effect_faint'):
        None('wild')
    prefix = '💥 치명타! ' if crit else ''
    move_name = attacker_entry.get('ultimate', '필살기') if ultimate else TYPE_SKILL_LABEL.get(attacker_types[0], '공격')
    attacker_type_mult = type_effect_multiplier(attacker_types[0], pokedex_types(entry)) + self.companion_type_bonus_pct(pokedex_types(entry)) / 100
    type_note = type_effect_note(attacker_type_mult)
    if ui.get('set_log'):
        None(f'''{prefix}{attacker_label}의 {move_name}! {dmg} 데미지!{type_note}''')
    if hp['wild'] <= 0:
        dex = ctx['dex']
        wild_level = ctx['wild_level']
        if self._catch_roll(entry, ctx['chosen_party']):
            if ui.get('set_log'):
                None(f'''{prefix}이겼다! 도감에 등록합니다...''')
            self._earn_gold(GOLD_PER_CATCH, source = 'catch')
            if ctx.get('is_shiny'):
                shiny_dict = self.state.setdefault('shiny_caught', { })
                prev_s = shiny_dict.get(str(dex))
                prev_s_level = prev_s.get('level', 0) if isinstance(prev_s, dict) else 0
                if prev_s or wild_level >= prev_s_level:
                    shiny_dict[str(dex)] = {
                        time.time: None(),
                        wild_level: 'caught_at' }
                if self.state.setdefault('dex', { }).get(str(dex)) not in ('caught',):
                    self.state['dex'][str(dex)] = 'seen'
            prev_player_level = player_level_from_state(self.state)
            record_catch_for_leveling(self.state, wild_level)
            if player_level_from_state(self.state) > prev_player_level:
            
                try:
                    self.trigger_fx('levelup')
                
                    try:
                        self.check_companion_leveling()
                        self.record_daily_action()
                        self.save_state()
                    
                        try:
                            self._check_and_show_gen_certificates()
                        
                            try:
                                self._popup_title_msgs(self._check_new_titles())
                                self._finish_battle(ctx, True, entered_fight = True)
                                return None
                                if ui.get('set_log'):
                                    None('전투에는 이겼지만... 놓쳐버렸다! 다음에 다시 도전해봐요.')
                                self._finish_battle(ctx, False, entered_fight = True)
                                return None
                                win.after(700, (lambda : self._wild_turn(ctx)))
                                return None
                                except Exception:
                                    ui['set_log'] if ui.get('set_log') else ui['set_log']
                                    continue
                                except Exception:
                                    ui['set_log'] if ui.get('set_log') else ui['set_log']
                                    continue
                                except Exception:
                                    ui['set_log'] if ui.get('set_log') else ui['set_log']
                                    continue
                            except Exception:
                                'level'
                                continue
