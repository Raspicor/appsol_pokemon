# module.PetApp._build_battle_code_payload
# source line 12827
# Recovered from bytecode; default argument values are not shown.

def _build_battle_code_payload(self):
    party = self._get_preset_dex_list('code')
    atk_pct = ()
    def_pct = companion_synergy_bonus(party, self.state.get('caught', { }), self.state.get('mega_party', []))
    if self.state.get('mega_evolved'):
        self.state.get('mega_evolved')
    [
        {
            'mega': bool(not self.state.get('custom_body_dex')),
            'crit': bs['crit'],
            'def': bs['def'],
            'atk': bs['atk'],
            'hp': bs['hp'],
            'level': self.body1_effective_level(),
            'name': self.display_name(),
            'dex': self.player_dex(),
            'kind': 'body' }] = self.player_battle_stats(atk_pct = atk_pct, def_pct = def_pct, crit_bonus = crit_pct)
    mega_set = (lambda .0: for x in .0:
    int(x).0)(self.state.get('mega_party', [])())
    caught = self.state.get('caught', { })
    for d in party:
        d = int(d)
        e = POKEDEX.get(d, { })
        lv = caught.get(str(d), { }).get('level', 1)
        if d in mega_set:
            d in mega_set
        is_mega = mega_companion_ready(d, caught)
        cbs = battle_stats(e, lv, extra_atk_pct = self.total_extra_atk_pct(), perm_atk_pct = perm_atk_bonus_pct(self.state), perm_all_mult = title_stat_mult(self.state), own_starter_stage = companion_stage_remaining(e), mega_mult = MEGA_BODY2_STAT_MULT if is_mega else 1, raised_bonus = self._is_raised(d))
        cbs = apply_title_battle_bonuses(cbs, self.state)
        nm = mega_companion_display_kr(d, e) if is_mega else e.get('kr', '?')
        roster.append({
            'mega': is_mega,
            'crit': cbs['crit'],
            'def': cbs['def'],
            'atk': cbs['atk'],
            'hp': cbs['hp'],
            'level': lv,
            'name': nm,
            'dex': d,
            'kind': 'companion' })
    set
    if self.state.get('mega_evolved'):
        self.state.get('mega_evolved')
    return {
        'roster': roster,
        'party': party,
        'dex': self.player_dex(),
        'mega': bool(not self.state.get('custom_body_dex')),
        'level': self.body1_effective_level(),
        'crit': bs['crit'],
        'def': bs['def'],
        'atk': bs['atk'],
        'hp': bs['hp'],
        'name': self.display_name() }
