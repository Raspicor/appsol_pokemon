# module.PetApp.open_pokedex._preview_wheel_scroll
# source line 16029
# Recovered from bytecode; default argument values are not shown.

def _preview_wheel_scroll(e):
    try:
        if preview_canvas.winfo_exists():
        
            try:
                preview_canvas.yview_scroll(int(-1 * (e.delta / 120)), 'units')
                return None
                return None
            except Exception:
                return None
