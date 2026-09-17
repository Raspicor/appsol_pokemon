# module.PetApp._refresh_minigame_hub
# source line 5526
# Recovered from bytecode; default argument values are not shown.

def _refresh_minigame_hub(self):
    win = getattr(self, '_active_minigame_hub_win', None)
    if win is None:
        return None

    try:
        alive = win.winfo_exists()
        self._active_minigame_hub_win = None
        if not alive:
            return None
    
        try:
            win.destroy()
            self.open_minigame_hub()
            return None
            except Exception:
                alive = False
                continue
        except Exception:
            continue
