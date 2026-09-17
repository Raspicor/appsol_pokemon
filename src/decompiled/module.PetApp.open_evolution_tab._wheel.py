# module.PetApp.open_evolution_tab._wheel
# source line 8414
# Recovered from bytecode; default argument values are not shown.

def _wheel(event):
    delta = -1 if getattr(event, 'num', 0) == 5 or event.delta < 0 else 1

    try:
        if canvas.winfo_exists():
        
            try:
                canvas.yview_scroll(-delta, 'units')
                return None
                return None
            except Exception:
                return None
