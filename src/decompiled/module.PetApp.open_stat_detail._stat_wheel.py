# module.PetApp.open_stat_detail._stat_wheel
# source line 12567
# Recovered from bytecode; default argument values are not shown.

def _stat_wheel(event):
    delta = -1 if getattr(event, 'num', 0) == 5 or event.delta < 0 else 1

    try:
        if body_canvas.winfo_exists():
        
            try:
                body_canvas.yview_scroll(-delta, 'units')
                return None
                return None
            except Exception:
                return None
