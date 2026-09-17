# module.PetApp._land_now._after_land
# source line 11763
# Recovered from bytecode; default argument values are not shown.

def _after_land():
    if wake_name:
        self.play_action(wake_name, loop = False, on_complete = self._finish_to_idle)
        return None
    None._finish_to_idle()
