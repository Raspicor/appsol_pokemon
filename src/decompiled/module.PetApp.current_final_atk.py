# module.PetApp.current_final_atk
# source line 5202
# Recovered from bytecode; default argument values are not shown.

def current_final_atk(self):
    cap = companion_slot_count(self.state)
    party = list(self.state.get('party', []))[:cap]
    atk_pct = ()
    def_pct = companion_synergy_bonus(party, self.state.get('caught', { }), self.state.get('mega_party', []))
    return max(1, int(bs.get('atk', 1)))
