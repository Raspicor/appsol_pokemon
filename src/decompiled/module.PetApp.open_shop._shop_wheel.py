# module.PetApp.open_shop._shop_wheel
# source line 13173
# Recovered from bytecode; default argument values are not shown.

def _shop_wheel(event):
    delta = -1 if getattr(event, 'num', 0) == 5 or event.delta < 0 else 1

    try:
        if outer_canvas.winfo_exists():
        
            try:
                outer_canvas.yview_scroll(-delta, 'units')
                return None
                return None
            except Exception:
                return None
