# module.PetApp.open_settings._on_hide
# source line 18876
# Recovered from bytecode; default argument values are not shown.

def _on_hide(*_a):
    self.state['pet_hide_seconds'] = hide_var.get()
    self.save_state()
