# module.PetApp._get_preset_slots
# source line 15125
# Recovered from bytecode; default argument values are not shown.

def _get_preset_slots(self, category):
    cap = self._preset_cap(category)
    raw = list(self.state.get('battle_presets', { }).get(category, []))[:cap]
    if len(raw) < cap:
        raw.append(None)
        continue
    return raw
