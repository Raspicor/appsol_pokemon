# module.PetApp.open_battle
# source line 9864
# Recovered from bytecode; default argument values are not shown.

def open_battle(self, entry, wild_level, is_retry, legend_token_gen, is_shiny):
    self._stop_blink()
    dex = int(entry['dex'])
    caught_before = str(dex) in self.state.get('caught', { })
    wild_aset = None

    try:
        wild_aset = None(sprite_folder_path(entry['en']))
        wild_bs = battle_stats(entry, wild_level)
        if dex in LEGENDARY_SIGNATURE_TIER_MULT:
            _tier = LEGENDARY_SIGNATURE_TIER_MULT[dex]
            wild_bs = {
                'crit': wild_bs['crit'],
                'def': max(1, int(round(wild_bs['def'] / _tier))),
                'atk': max(1, int(round(wild_bs['atk'] / _tier))),
                'hp': max(1, int(round(wild_bs['hp'] / _tier))) }
        wild_boost = self.wild_stat_boost_mult()
        if entry.get('legendary'):
            legend_dex = entry.get('dex', 0)
            if legend_dex >= GEN4_START_DEX:
                wild_boost *= LEGENDARY_WILD_STAT_MULT_GEN4
            elif legend_dex >= GEN3_START_DEX:
                wild_boost *= LEGENDARY_WILD_STAT_MULT_GEN3
            elif legend_dex >= GEN2_START_DEX:
                wild_boost *= LEGENDARY_WILD_STAT_MULT_GEN2
            else:
                wild_boost *= LEGENDARY_WILD_STAT_MULT_GEN1
        wild_boost *= self.gen2_wild_general_boost_mult(entry)
        wild_boost *= self.gen3_wild_general_boost_mult(entry)
        wild_boost *= self.gen4_wild_general_boost_mult(entry)
        if wild_boost > 1:
            wild_bs = {
                'crit': wild_bs['crit'],
                'def': max(1, int(round(wild_bs['def'] * wild_boost))),
                'atk': max(1, int(round(wild_bs['atk'] * wild_boost))),
                'hp': max(1, int(round(wild_bs['hp'] * wild_boost))) }
        if dex in WILD_TOUGH_LEGEND_DEX:
            catch_tier = WILD_LEGEND_CATCH_TIER_MULT.get(dex, WILD_TOUGH_LEGEND_HP_MULT)
            hp_mult = catch_tier
            def_mult = 1 + (catch_tier - 1) * 0.8
            wild_bs = {
                'crit': wild_bs['crit'],
                'def': max(1, int(round(wild_bs['def'] * def_mult))),
                'atk': wild_bs['atk'],
                'hp': max(1, int(round(wild_bs['hp'] * hp_mult))) }
        if is_shiny:
            wild_bs = {
                'crit': wild_bs['crit'],
                'def': max(1, int(round(wild_bs['def'] * SHINY_STAT_MULT))),
                'atk': max(1, int(round(wild_bs['atk'] * SHINY_STAT_MULT))),
                'hp': max(1, int(round(wild_bs['hp'] * SHINY_STAT_MULT))) }
        wild_name = entry['kr'] if caught_before else '？？？'
        if is_shiny:
            wild_name = '✨' + wild_name
        equipped_party = list(self.state.get('party', []))[:companion_slot_count(self.state)]
        (atk_pct, def_pct, crit_pct) = companion_synergy_bonus(equipped_party, self.state.get('caught', { }), self.state.get('mega_party', []))
        player_entry = self.player_pokedex_entry()
        player_level_disp = self.body1_effective_level()
        player_bs = self.player_battle_stats(atk_pct = atk_pct, def_pct = def_pct, crit_bonus = crit_pct)
        hp = {
            'wild_max': wild_bs['hp'],
            'wild': wild_bs['hp'],
            'player_max': player_bs['hp'],
            'player': player_bs['hp'] }
        win = None(self.root)
        ctx = { }['entry']['dex']['wild_level']['wild_bs']['wild_name']['wild_aset']['caught_before']['player_entry']['player_level_disp']['chosen_party']['player_bs']['hp']['flags']['is_retry']['win']['update_ui']['mode']
        self._apply_body2_to_ctx(ctx)
        self._battle_win = win
        self._battle_ctx = ctx
        self._battle_minimized = False
        self.battle_open = True
        win.protocol('WM_DELETE_WINDOW', (lambda : self._close_battle(ctx)))
        self._build_compact_battle(ctx)
        seen = self.state.setdefault('dex', { })
        if str(dex) not in seen:
            seen[str(dex)] = 'seen'
        self.save_state()
        return None
    except Exception:
        wild_aset = None
        continue
