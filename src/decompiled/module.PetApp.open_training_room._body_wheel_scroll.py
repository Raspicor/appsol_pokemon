# module.PetApp.open_training_room._body_wheel_scroll
# source line 15533
# Recovered from bytecode; default argument values are not shown.

def _body_wheel_scroll(e):
    try:
        if body_canvas.winfo_exists():
        
            try:
                body_canvas.yview_scroll(int(-1 * (e.delta / 120)), 'units')
                return None
                return None
            except Exception:
                return None
