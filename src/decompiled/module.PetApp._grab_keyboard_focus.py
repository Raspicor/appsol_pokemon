# module.PetApp._grab_keyboard_focus
# source line 9167
# Recovered from bytecode; default argument values are not shown.

def _grab_keyboard_focus(self):
    def _try():
    
        try:
            self.root.lift()
            self.root.focus_force()
            self.label.focus_set()
            return None
        except Exception:
            return None


    None()
    for delay_ms in (60, 200, 500, 900):
        self.root.after(delay_ms, _try)
    _try
    return None
    except Exception:
        continue
