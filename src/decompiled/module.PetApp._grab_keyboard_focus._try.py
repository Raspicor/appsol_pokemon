# module.PetApp._grab_keyboard_focus._try
# source line 9175
# Recovered from bytecode; default argument values are not shown.

def _try():
    try:
        self.root.lift()
        self.root.focus_force()
        self.label.focus_set()
        return None
    except Exception:
        return None
