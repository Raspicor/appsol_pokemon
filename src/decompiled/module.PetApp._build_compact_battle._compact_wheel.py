# module.PetApp._build_compact_battle._compact_wheel
# source line 10117
# Recovered from bytecode; default argument values are not shown.

def _compact_wheel(event):
    delta = -1 if getattr(event, 'num', 0) == 5 or event.delta < 0 else 1

    try:
        if canvas.winfo_exists():
        
            try:
                canvas.yview_scroll(-delta, 'units')
                return None
                return None
            except Exception:
                return None
