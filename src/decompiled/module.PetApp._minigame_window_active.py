# module.PetApp._minigame_window_active
# source line 5493
# Recovered from bytecode; default argument values are not shown.

def _minigame_window_active(self):
    win = getattr(self, '_active_minigame_win', None)
    if win is not None:
    
        try:
            if win.winfo_exists():
            
                try:
                    win.lift()
                    win.focus_force()
                    return True
                    self._active_minigame_win = None
                    return False
                except Exception:
                    continue
