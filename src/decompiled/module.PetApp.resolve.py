# module.PetApp.resolve
# source line 4862
# Recovered from bytecode; default argument values are not shown.

def resolve(self, logical):
    val = self.stage_conf().get(logical)
    if val:
        return val
    if None == 'happy':
        return self._pick_dynamic_action(HAPPY_ACTION_CANDIDATES)
    if None == 'hungry':
        return self._pick_dynamic_action(HUNGRY_ACTION_CANDIDATES)
