# module.PetApp._maybe_notify_training_done
# source line 9408
# Recovered from bytecode; default argument values are not shown.

def _maybe_notify_training_done(self):
    start = self.state.get('train_session_start', 0)
    if not start:
        return None
    if None() - start < TRAIN_SESSION_SECONDS:
        return None
    if None.time._train_done_notified_at == start:
        return None
    None._train_done_notified_at = None
    win = getattr(self, '_active_training_win', None)

    try:
        if win is not None and win.winfo_exists():
            return None
        None._show_training_done_toast()
        return None
    except Exception:
        continue
