# module.PetApp._show_training_done_toast._dismiss
# source line 9558
# Recovered from bytecode; default argument values are not shown.

def _dismiss():
    w = getattr(self, '_train_done_toast_win', None)
    if w is not None:
        self._train_done_toast_win = None
    
        try:
            w.destroy()
            return None
            return None
        except Exception:
            return None
