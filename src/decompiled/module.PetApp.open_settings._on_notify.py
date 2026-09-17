# module.PetApp.open_settings._on_notify
# source line 18769
# Recovered from bytecode; default argument values are not shown.

def _on_notify(*_a):
    self.state['encounter_notify_mode'] = notify_var.get()
    self.save_state()
