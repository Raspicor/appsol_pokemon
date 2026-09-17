# module.PetApp.use_skill
# source line 11841
# Recovered from bytecode; default argument values are not shown.

def use_skill(self):
    if self.behavior_state in ('held', 'falling') or self.battle_open:
        return None
    None._do_one_shot('skill')
