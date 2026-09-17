# module.resolve_species_win
# source line 3947
# Recovered from bytecode; default argument values are not shown.

def resolve_species_win(win, min_w, min_h):
    try:
        win.update_idletasks()
        sw = win.winfo_screenwidth()
        sh = win.winfo_screenheight()
        win.minsize(min(min_w, sw - 40), min(min_h, sh - 80))
        win.resizable(True, True)
        return None
    except Exception:
        return None
