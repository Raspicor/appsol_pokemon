# module.PetApp._set_preset_slot
# source line 15155
# Recovered from bytecode; default argument values are not shown.

def _set_preset_slot(self, category, slot_idx, dex_or_none):
    presets = self.state.setdefault('battle_presets', { })
    slots = self._get_preset_slots(category)
    if  <= 0, slot_idx or 0, slot_idx < len(slots):
        pass

    slots = dex_or_none
    self.save_state()
