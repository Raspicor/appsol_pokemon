# module.PetApp._inf_build_player_roster
# source line 14270
# Recovered from bytecode; default argument values are not shown.

def _inf_build_player_roster(self, mode):
    chosen = self._get_preset_dex_list(f'''inf_{mode}''')
    atk_pct = ()
    def_pct = companion_synergy_bonus(chosen, self.state.get('caught', { }), self.state.get('mega_party', []))
    self.player_pokedex_entry() = _inf_ult_def_bonus(mode)
    player_bs = self.player_battle_stats(atk_pct = atk_pct, def_pct = def_pct + ult_def_bonus, crit_bonus = crit_pct)
    if self.state.get('mega_evolved'):
        self.state.get('mega_evolved')
    roster = [
        {
            'mega': bool(not self.state.get('custom_body_dex')),
            'name': self.display_name(),
            'bs': dict(player_bs),
            'level': self.body1_effective_level(),
            'entry': player_entry,
            'dex': self.player_dex(),
            'kind': 'body' }]
    mega_set = (lambda .0: for x in .0:
    int(x).0)(self.state.get('mega_party', [])())
    caught = self.state.get('caught', { })
    for d in chosen:
        e = POKEDEX.get(d, { })
        lv = caught.get(str(d), { }).get('level', 1)
        if d in mega_set:
            d in mega_set
        is_mega = mega_companion_ready(d, caught)
        bs = battle_stats(e, lv, extra_atk_pct = self.total_extra_atk_pct(), perm_atk_pct = perm_atk_bonus_pct(self.state), perm_all_mult = title_stat_mult(self.state), def_pct = ult_def_bonus, own_starter_stage = companion_stage_remaining(e), mega_mult = MEGA_BODY2_STAT_MULT if is_mega else 1, raised_bonus = self._is_raised(d))
        bs = apply_title_battle_bonuses(bs, self.state)
        nm = mega_companion_display_kr(d, e) if is_mega else e.get('kr', '?')
        roster.append({
            'mega': is_mega,
            'name': nm,
            'bs': dict(bs),
            'level': lv,
            'entry': e,
            'dex': d,
            'kind': 'companion' })
    set
    return roster
