# module.PetApp._apply_body2_to_ctx
# source line 9812
# Recovered from bytecode; default argument values are not shown.

def _apply_body2_to_ctx(self, ctx, chosen_party):
    dex2 = second_body_equipped_dex(self.state)
    if not dex2:
        ctx['has_body2'] = False
        ctx['body2_entry'] = None
        ctx['hp'].pop('body2', None)
        ctx['hp'].pop('body2_max', None)
        return None
    e2 = None.get(int(dex2))
    if not e2:
        ctx['has_body2'] = False
        ctx['body2_entry'] = None
        ctx['hp'].pop('body2', None)
        ctx['hp'].pop('body2_max', None)
        return None
    if None is None:
        if not ctx.get('chosen_party'):
            ctx.get('chosen_party')
        chosen_party = list(self.state.get('party', []))[:companion_slot_count(self.state)]
    atk_pct = ()
    def_pct = companion_synergy_bonus(chosen_party, self.state.get('caught', { }), self.state.get('mega_party', []))
    if bool(self.state.get('mega_body2')):
        bool(self.state.get('mega_body2'))
    mega_companion_ready(dex2, self.state.get('caught', { })) = self.player_level()
    bs2 = battle_stats(e2, lv2, atk_pct = atk_pct, def_pct = def_pct, crit_bonus = crit_pct, extra_atk_pct = self.total_extra_atk_pct(), perm_atk_pct = perm_atk_bonus_pct(self.state), perm_all_mult = title_stat_mult(self.state), own_starter_stage = companion_stage_remaining(e2), mega_mult = MEGA_BODY2_STAT_MULT if is_mega2 else 1, raised_bonus = self._is_raised(dex2))
    bs2 = apply_title_battle_bonuses(bs2, self.state)
    ctx['has_body2'] = True
    ctx['body2_entry'] = e2
    ctx['body2_level_disp'] = lv2
    ctx['body2_bs'] = bs2
    ctx['body2_mega'] = is_mega2
    ctx['hp']['body2'] = bs2['hp']
    ctx['hp']['body2_max'] = bs2['hp']
    aset_key = (int(dex2), is_mega2)
    if ctx.get('body2_aset_key') != aset_key:
        sprite_name = e2['en']
        if is_mega2:
            mega_folder = companion_mega_sprite_folder(e2)
            if mega_folder:
                sprite_name = mega_folder
    
        try:
            ctx['body2_aset'] = None(sprite_folder_path(sprite_name))
            ctx['body2_aset_key'] = aset_key
            ctx['body2_aset_dex'] = int(dex2)
            return None
            return None
        except Exception:
            ctx['body2_aset'] = None
            continue
