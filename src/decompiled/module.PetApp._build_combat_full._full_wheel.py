# module.PetApp._build_combat_full._full_wheel
# source line 10646
# Recovered from bytecode; default argument values are not shown.

def _full_wheel(event):
    delta = -1 if getattr(event, 'num', 0) == 5 or event.delta < 0 else 1

    try:
        if canvas.winfo_exists():
        
            try:
                canvas.yview_scroll(-delta, 'units')
                return None
                return None
            except Exception:
                return None
