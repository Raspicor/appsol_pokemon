# module.PetApp._show_food_boost_done_toast._dismiss
# source line 9605
# Recovered from bytecode; default argument values are not shown.

def _dismiss():
    w = getattr(self, '_food_done_toast_win', None)
    if w is not None:
        self._food_done_toast_win = None
    
        try:
            w.destroy()
            return None
            return None
        except Exception:
            return None
