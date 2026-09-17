# module.PetApp.my_type_effect_mult
# source line 4853
# Recovered from bytecode; default argument values are not shown.

def my_type_effect_mult(self, defender_types):
    base = type_effect_multiplier(self.current_element(), defender_types)
    return base + self.companion_type_bonus_pct(defender_types) / 100
