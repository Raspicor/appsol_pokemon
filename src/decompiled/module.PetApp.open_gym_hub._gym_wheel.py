# module.PetApp.open_gym_hub._gym_wheel
# source line 16821
# Recovered from bytecode; default argument values are not shown.

def _gym_wheel(event):
    delta = -1 if getattr(event, 'num', 0) == 5 or event.delta < 0 else 1

    try:
        if canvas.winfo_exists():
        
            try:
                canvas.yview_scroll(-delta, 'units')
                return None
                return None
            except Exception:
                return None
