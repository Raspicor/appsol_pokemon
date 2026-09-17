# module.PetApp._clear_active_minigame_win
# source line 5508
# Recovered from bytecode; default argument values are not shown.

def _clear_active_minigame_win(self, win):
    if getattr(self, '_active_minigame_win', None) is win:
        self._active_minigame_win = None
        return None
