# module.PetApp._legend_token_roll_level
# source line 13484
# Recovered from bytecode; default argument values are not shown.

def _legend_token_roll_level(self, gen):
    if all_gen2_caught(self.state):
        pass
    elif all_gen1_caught(self.state):
        pass

    lvl_cap = 5
    low = min(LEGEND_TOKEN_MIN_LEVEL.get(gen, 5), lvl_cap)
    return None(low, max(low, lvl_cap))
