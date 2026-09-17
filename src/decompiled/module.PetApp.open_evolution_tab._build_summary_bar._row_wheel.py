# module.PetApp.open_evolution_tab._build_summary_bar._row_wheel
# source line 8893
# Recovered from bytecode; default argument values are not shown.

def _row_wheel(event):
    delta = -1 if getattr(event, 'num', 0) == 5 or event.delta < 0 else 1

    try:
        if row_canvas.winfo_exists():
        
            try:
                row_canvas.xview_scroll(-delta, 'units')
                return None
                return None
            except Exception:
                return None
