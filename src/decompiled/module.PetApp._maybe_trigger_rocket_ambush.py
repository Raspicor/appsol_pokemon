# module.PetApp._maybe_trigger_rocket_ambush
# source line 13891
# Recovered from bytecode; default argument values are not shown.

def _maybe_trigger_rocket_ambush(self, dt):
    if self.state.get('rocket_ambush_location') == 'off':
        return None
    if None.battle_open and self.state.get('in_ball') or self._pending_encounter:
        return None
    if None(self, '_omok_open', False):
        return None
    if None.behavior_state in ('held', 'falling', 'sleep'):
        return None
    if not None._get_preset_dex_list('rocket'):
        return None
    now = None()
    if now - self.state.get('rocket_last_encounter_at', 0) < ROCKET_AMBUSH_COOLDOWN:
        return None
    if None() < ROCKET_AMBUSH_CHANCE_PER_SEC * dt:
        self.state['rocket_last_encounter_at'] = now
        self.save_state()
        self._show_rocket_toast()
        return None
    return None.time.random
