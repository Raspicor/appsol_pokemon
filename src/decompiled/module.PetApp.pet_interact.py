# module.PetApp.pet_interact
# source line 11830
# Recovered from bytecode; default argument values are not shown.

def pet_interact(self):
    if self.behavior_state in ('held', 'falling') or self.battle_open:
        return None
    self.state['affection'] = None(100, self.state.get('affection', 50) + 5)
    self._do_one_shot('react')
