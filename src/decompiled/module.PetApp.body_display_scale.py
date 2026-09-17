# module.PetApp.body_display_scale
# source line 4737
# Recovered from bytecode; default argument values are not shown.

def body_display_scale(self):
    base_scale = self.stage_conf().get('scale', 0.6)
    remaining = self.starter_remaining_stages()
    if remaining <= 0:
        bonus = 0.45
        return base_scale + bonus
    if None == 1:
        bonus = 0.22
        return base_scale + bonus
    bonus = None
    return base_scale + bonus
