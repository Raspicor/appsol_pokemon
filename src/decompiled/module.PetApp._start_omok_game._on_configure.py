# module.PetApp._start_omok_game._on_configure
# source line 6718
# Recovered from bytecode; default argument values are not shown.

def _on_configure(event):
    job = ctx.get('resize_job')
    if job is not None:
    
        try:
            win.after_cancel(job)
            ctx['resize_job'] = win.after(120, _redraw_board)
            return None
        except Exception:
            continue
