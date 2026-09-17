# module.PetApp._start_omok_game._on_close
# source line 6747
# Recovered from bytecode; default argument values are not shown.

def _on_close():
    ctx['closed'] = True
    None()
    None()
    self._omok_open = False
    self._clear_active_minigame_win(win)

    try:
        win.destroy()
        return None
    except Exception:
        _cancel_ai_job
        return None
