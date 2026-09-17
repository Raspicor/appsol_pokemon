# module.PetApp.open_game_quiz._cancel
# source line 6224
# Recovered from bytecode; default argument values are not shown.

def _cancel():
    if ctx['job'] is not None:
    
        try:
            win.after_cancel(ctx['job'])
            ctx['job'] = None
            return None
            return None
        except Exception:
            continue
