# module.PetApp._start_omok_game._cancel_resize_job
# source line 6738
# Recovered from bytecode; default argument values are not shown.

def _cancel_resize_job():
    job = ctx.get('resize_job')
    if job is not None:
    
        try:
            win.after_cancel(job)
            ctx['resize_job'] = None
            return None
            return None
        except Exception:
            continue
