# module.PetApp.open_mega_evolve._switch_mega_form
# source line 12429
# Recovered from bytecode; default argument values are not shown.

def _switch_mega_form(f):
    if self.state.get('mega_form') == f:
        return None
    self.state['mega_form'] = None
    self.save_state()

    try:
        self.redraw()
        if not self.mega_display_name_for():
            self.mega_display_name_for()
        form_label_var.set(f'''지금 폼: {'?'}''')
        return None
    except Exception:
        continue
