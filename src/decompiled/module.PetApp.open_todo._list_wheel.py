# module.PetApp.open_todo._list_wheel
# source line 18612
# Recovered from bytecode; default argument values are not shown.

def _list_wheel(event):
    delta = -1 if getattr(event, 'num', 0) == 5 or event.delta < 0 else 1

    try:
        if list_canvas.winfo_exists():
        
            try:
                list_canvas.yview_scroll(-delta, 'units')
                return None
                return None
            except Exception:
                return None
