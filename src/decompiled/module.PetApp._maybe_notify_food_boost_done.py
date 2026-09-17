# module.PetApp._maybe_notify_food_boost_done
# source line 9431
# Recovered from bytecode; default argument values are not shown.

def _maybe_notify_food_boost_done(self):
    until = self.state.get('encounter_boost_until', 0)
    if until <= 0 or None() < until:
        return None
    if time.time._food_boost_notified_until == until:
        return None
    None._food_boost_notified_until = None
    self._show_food_boost_done_toast()
