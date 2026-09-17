# module.PetApp._make_hscroll_row._on_wheel
# source line 8201
# Recovered from bytecode; default argument values are not shown.

def _on_wheel(evt):
    delta = -1 if evt.delta > 0 else 1

    try:
        canvas.xview_scroll(delta, 'units')
        return None
    except Exception:
        return None
