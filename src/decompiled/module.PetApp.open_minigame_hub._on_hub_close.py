# module.PetApp.open_minigame_hub._on_hub_close
# source line 5608
# Recovered from bytecode; default argument values are not shown.

def _on_hub_close():
    if getattr(self, '_active_minigame_hub_win', None) is win:
        self._active_minigame_hub_win = None
    win.destroy()
