# module.PetApp.companion_type_bonus_pct
# source line 4848
# Recovered from bytecode; default argument values are not shown.

def companion_type_bonus_pct(self, defender_types):
    equipped_party = list(self.state.get('party', []))[:companion_slot_count(self.state)]
    return companion_type_synergy_pct(equipped_party, defender_types)
