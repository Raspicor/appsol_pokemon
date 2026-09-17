# module.PetApp.player_battle_stats
# source line 5161
# Recovered from bytecode; default argument values are not shown.

def player_battle_stats(self, atk_pct, def_pct, crit_bonus):
    extra_atk_pct = self.total_extra_atk_pct()
    perm_atk_pct = perm_atk_bonus_pct(self.state)
    perm_all_mult = title_stat_mult(self.state)
    t_def_pct = title_def_bonus_pct(self.state)
    t_crit_pct = title_crit_bonus_pct(self.state)
    t_hp_pct = title_hp_pct_bonus(self.state)
    t_hp_flat = title_hp_flat_bonus(self.state)
    custom_dex = self.state.get('custom_body_dex')
    if custom_dex:
        entry = POKEDEX.get(int(custom_dex), self.player_pokedex_entry())
        own_level = self.body1_effective_level()
        bs = battle_stats(entry, own_level, atk_pct = atk_pct, def_pct = def_pct + t_def_pct, crit_bonus = crit_bonus + t_crit_pct, extra_atk_pct = extra_atk_pct, own_starter_stage = None, mega_mult = 1, perm_atk_pct = perm_atk_pct, raised_bonus = self._is_raised(custom_dex), perm_all_mult = perm_all_mult)
    else:
        lvl = self.player_level()
        mm = self.mega_mult()
        (mega_atk_mm, mega_def_mm) = self.mega_atk_def_mult()
        bs = battle_stats(self.player_pokedex_entry(), lvl, atk_pct = atk_pct, def_pct = def_pct + t_def_pct, crit_bonus = crit_bonus + t_crit_pct, extra_atk_pct = extra_atk_pct, mega_atk_mult = mega_atk_mm, mega_def_mult = mega_def_mm, own_starter_stage = self.starter_remaining_stages(), mega_mult = mm, perm_atk_pct = perm_atk_pct, perm_all_mult = perm_all_mult)
    if t_hp_pct:
        bs['hp'] = max(1, int(round(bs['hp'] * (1 + t_hp_pct / 100))))
    if t_hp_flat:
        bs['hp'] = max(1, int(round(bs['hp'] + t_hp_flat)))
    return bs
