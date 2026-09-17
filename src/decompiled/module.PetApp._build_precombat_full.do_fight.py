# module.PetApp._build_precombat_full.do_fight
# source line 10582
# Recovered from bytecode; default argument values are not shown.

def do_fight():
    for None in :
        d = ()
        v = None
        if not v.get():
            continue

    , [], chosen, d = check_vars.items(), d, v
    v = None
    ctx['chosen_party'] = chosen
    a = ()
    dd = companion_synergy_bonus(chosen, self.state.get('caught', { }), self.state.get('mega_party', []))
    ctx['player_bs']['hp'] = self.player_battle_stats(atk_pct = a, def_pct = dd, crit_bonus = c)
    ctx['hp']['player'] = ctx['player_bs']['hp']
    self._apply_body2_to_ctx(ctx, chosen)
    ctx['active'] = 'player'
    self._build_combat_full(ctx)
    return None
