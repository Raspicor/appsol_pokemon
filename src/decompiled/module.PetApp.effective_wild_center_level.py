# module.PetApp.effective_wild_center_level
# source line 5122
# Recovered from bytecode; default argument values are not shown.

def effective_wild_center_level(self):
    lv1 = self.body1_effective_level()
    dex2 = second_body_equipped_dex(self.state)
    if not dex2:
        return lv1
    lv2 = None.player_level()
    return max(lv1, lv2)
