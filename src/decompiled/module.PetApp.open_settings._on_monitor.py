# module.PetApp.open_settings._on_monitor
# source line 18804
# Recovered from bytecode; default argument values are not shown.

def _on_monitor(*_a):
    v = monitor_var.get()
    self.set_single_monitor_mode(v == 'single')
    self.set_secondary_monitor_mode(v == 'secondary')
