# module.PetApp.open_game_feed._on_close
# source line 5912
# Recovered from bytecode; default argument values are not shown.

def _on_close():
    ctx['closed'] = True
    None()
    self._clear_active_minigame_win(win)
    win.destroy()
