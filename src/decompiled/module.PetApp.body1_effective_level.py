# module.PetApp.body1_effective_level
# source line 5111
# Recovered from bytecode; default argument values are not shown.

def body1_effective_level(self):
    custom_dex = self.state.get('custom_body_dex')
    if custom_dex:
        return int(self.state.get('caught', { }).get(str(int(custom_dex)), { }).get('level', 1))
    return None.player_level()
