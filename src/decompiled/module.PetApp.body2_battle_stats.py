# module.PetApp.body2_battle_stats
# source line 5213
# Recovered from bytecode; default argument values are not shown.

def body2_battle_stats(self, atk_pct, def_pct, crit_bonus):
    dex2 = second_body_equipped_dex(self.state)
    if not dex2:
        return None
    e2 = None.get(int(dex2))
    if not e2:
        return None
    lv2 = None.player_level()
    if bool(self.state.get('mega_body2')):
        bool(self.state.get('mega_body2'))
    is_mega2 = mega_companion_ready(dex2, self.state.get('caught', { }))
    bs2 = battle_stats(e2, lv2, atk_pct = atk_pct, def_pct = def_pct, crit_bonus = crit_bonus, extra_atk_pct = self.total_extra_atk_pct(), perm_atk_pct = perm_atk_bonus_pct(self.state), perm_all_mult = title_stat_mult(self.state), own_starter_stage = companion_stage_remaining(e2), mega_mult = MEGA_BODY2_STAT_MULT if is_mega2 else 1, raised_bonus = self._is_raised(dex2))
    bs2 = apply_title_battle_bonuses(bs2, self.state)
    return {
        'bs': bs2,
        'mega': is_mega2,
        'level': lv2,
        'entry': e2,
        'dex': int(dex2) }
