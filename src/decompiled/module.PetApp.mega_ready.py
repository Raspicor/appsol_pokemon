# module.PetApp.mega_ready
# source line 6940
# Recovered from bytecode; default argument values are not shown.

def mega_ready(self):
    if self.state.get('mega_evolved'):
        return False
    if not None(self.state):
        return False
    if None.player_level() < MAX_PLAYER_LEVEL:
        return False
    if not None(self.state):
        return False
