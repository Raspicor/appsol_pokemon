# module.PetApp._ask_mega_form_choice._pick
# source line 11135
# Recovered from bytecode; default argument values are not shown.

def _pick(form):
    result['form'] = form

    try:
        win.grab_release()
        win.destroy()
        return None
    except Exception:
        continue
