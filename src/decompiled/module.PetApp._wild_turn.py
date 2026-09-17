# module.PetApp._wild_turn
# source line 11063
# Recovered from bytecode; default argument values are not shown.

def _wild_turn(self, ctx):
    flags = ctx['flags']
    ui = ctx['update_ui']
    if not ctx['hp']['wild'] <= 0 or any_body_alive(ctx):
        flags['locked'] = False
        if ui.get('set_locked'):
            None(False)
        return None
    wild_bs = None['wild_bs']
    target = ctx.get('active', 'player')
    target_bs = body_bs(ctx, target)
    target_entry = body_entry(ctx, target)
    wild_types = pokedex_types(ctx['entry'])
    wdmg = ()
    wcrit = compute_damage(wild_bs['atk'], target_bs['def'], wild_bs['crit'], defending = flags['defending'], attacker_type = wild_types[0], defender_types = pokedex_types(target_entry))
    max(0, body_hp(ctx, target) - wdmg) = False
    set_body_hp(ctx, target, new_hp)
    if ui.get('effect'):
        None('wild', crit = wcrit)
    prefix = '💥 치명타! ' if wcrit else ''
    w_type_mult = type_effect_multiplier(wild_types[0], pokedex_types(target_entry))
    w_type_note = type_effect_note(w_type_mult)
    target_label = f'''내 {self.display_name()}''' if target == 'player' else f'''내 {target_entry.get('kr', '2번 본체')}'''
    msg = f'''{prefix}야생 {ctx['wild_name']}의 반격! {target_label}에게 {wdmg} 데미지!{w_type_note}'''
    if not any_body_alive(ctx):
        if ui.get('set_log'):
            None(msg + ' 본체가 모두 쓰러져 도망쳤다...')
        if ui.get('refresh_bars'):
            None()
        self._finish_battle(ctx, False, entered_fight = True)
        return None
    fainted_now = ui['effect'] <= 0
    if fainted_now and ui.get('effect_faint'):
        None(target)
    ctx['active'] = next_active_body(ctx)
    if fainted_now:
        new_active_entry = body_entry(ctx, ctx['active'])
        new_active_label = f'''내 {self.display_name()}''' if ctx['active'] == 'player' else f'''내 {new_active_entry.get('kr', '2번 본체')}'''
        msg += f''' {target_label}이(가) 쓰러졌다! {new_active_label}이(가) 이어서 싸운다!'''
    if ui.get('set_log'):
        None(msg)
    if ui.get('refresh_bars'):
        None()
    if ui.get('refresh_ult'):
        None()
    flags['locked'] = False
    if ui.get('set_locked'):
        None(False)
        return None
    return ui['refresh_ult']
