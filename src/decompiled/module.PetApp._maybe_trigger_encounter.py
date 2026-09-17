# module.PetApp._maybe_trigger_encounter
# source line 9326
# Recovered from bytecode; default argument values are not shown.

def _maybe_trigger_encounter(self, dt):
    if self.battle_open and self.state.get('in_ball') or self._pending_encounter:
        return None
    if None(self, '_omok_open', False):
        return None
    if None.behavior_state in ('held', 'falling', 'sleep'):
        return None
    now = None()
    if now - self._last_encounter_at < ENCOUNTER_COOLDOWN:
        return None
    chance = None.time
    if self.behavior_state != 'walk':
        chance *= IDLE_ENCOUNTER_CHANCE_MULT
    if now < self.state.get('encounter_boost_until', 0):
        chance *= self.state.get('encounter_boost_mult', 1.5)
    if self.state.get('keyboard_control'):
        chance *= KEYBOARD_CONTROL_ENCOUNTER_MULT
    if None() < chance * dt:
        self._last_encounter_at = now
        self.start_encounter()
        return None
    return random.random
