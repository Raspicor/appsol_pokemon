# module.PetApp.trick
# source line 11836
# Recovered from bytecode; default argument values are not shown.

def trick(self):
    if self.behavior_state in ('held', 'falling') or self.battle_open:
        return None
    None._do_one_shot('trick')
