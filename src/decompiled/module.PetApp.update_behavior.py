# module.PetApp.update_behavior
# source line 9046
# Recovered from bytecode; default argument values are not shown.

def update_behavior(self, dt, now):
    self._maybe_trigger_encounter(dt)
    self._maybe_trigger_rocket_ambush(dt)
    self._maybe_notify_training_done()
    self._maybe_notify_food_boost_done()
    self._maybe_notify_todo_alarms(now)
    if self.behavior_state == 'held':
        return None
    if None.behavior_state == 'falling':
        if self.state.get('keyboard_control'):
            self._kb_apply_air_move(dt)
        self._update_falling(dt)
        return None
    if None.behavior_state in ('jump', 'acting'):
        return None
    if None.state.get('keyboard_control'):
        self._update_keyboard_move(dt)
        return None
    if None.behavior_state == 'walk':
        self._update_walk(dt)
        return None
    if None.behavior_state == 'sleep':
        self._update_sleep(now)
        return None
    if None.behavior_state == 'idle':
        if now >= self.idle_next_decision_at:
            self.pick_next_from_idle()
        return None
