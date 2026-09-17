# module.PetApp.open_status._bind_status_wheel
# source line 18405
# Recovered from bytecode; default argument values are not shown.

def _bind_status_wheel(evt):
    try:
        outer_canvas.bind_all('<MouseWheel>', _on_status_wheel)
        return None
    except Exception:
        return None
