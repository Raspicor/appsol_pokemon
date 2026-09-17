# module.PetApp._start_omok_game._cancel_ai_job
# source line 6729
# Recovered from bytecode; default argument values are not shown.

def _cancel_ai_job():
    job = ctx.get('ai_job')
    if job is not None:
    
        try:
            win.after_cancel(job)
            ctx['ai_job'] = None
            return None
            return None
        except Exception:
            continue
