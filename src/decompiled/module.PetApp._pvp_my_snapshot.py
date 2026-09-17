# module.PetApp._pvp_my_snapshot
# source line 17664
# Recovered from bytecode; default argument values are not shown.

def _pvp_my_snapshot(self):
    cap = companion_slot_count(self.state)
    party = list(self.state.get('party', []))[:cap]
    atk_pct = ()
    def_pct = companion_synergy_bonus(party, self.state.get('caught', { }), self.state.get('mega_party', []))
    return {
        'party_names': self._pvp_my_party_names(),
        'crit': float(bs.get('crit', 15)),
        'def': max(1, int(bs['def'])),
        'atk': max(1, int(bs['atk'])),
        'hp': max(1, int(bs['hp'])),
        'level': self.player_level(),
        'name': self.display_name(),
        'type': 'roster' }
