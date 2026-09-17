# module.PetApp._minigame_played_today
# source line 5463
# Recovered from bytecode; default argument values are not shown.

def _minigame_played_today(self, key):
    return self._minigame_ensure_daily().get(key) is not None
