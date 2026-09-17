# module.PetApp.open_training_room._on_body_configure
# source line 15524
# Recovered from bytecode; default argument values are not shown.

def _on_body_configure(evt):
    body_canvas.configure(scrollregion = body_canvas.bbox('all'))

    try:
        body_canvas.itemconfigure(_body_win_id, width = body_canvas.winfo_width())
        return None
    except Exception:
        return None
