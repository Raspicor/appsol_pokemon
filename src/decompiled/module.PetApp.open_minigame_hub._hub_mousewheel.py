# module.PetApp.open_minigame_hub._hub_mousewheel
# source line 5631
# Recovered from bytecode; default argument values are not shown.

def _hub_mousewheel(event):
    delta = -1 if event.num == 5 or event.delta < 0 else 1

    try:
        if hub_canvas.winfo_exists():
        
            try:
                hub_canvas.yview_scroll(-delta, 'units')
                return None
                return None
            except Exception:
                return None
