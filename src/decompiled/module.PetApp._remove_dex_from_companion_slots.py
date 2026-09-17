# module.PetApp._remove_dex_from_companion_slots
# source line 4780
# Recovered from bytecode; default argument values are not shown.

def _remove_dex_from_companion_slots(self, dex):
    dex = int(dex)
    changed = False
    for None in party_now,:
        if not int(d) != dex:
            continue
    party_now, = , []
    d = self.state.get('party', []), d
    if len(party_now) != len(self.state.get('party', [])):
        self.state['party'] = party_now
        changed = True
    presets = self.state.setdefault('battle_presets', { })
    for _cat in PRESET_CATEGORIES:
        _slots = list(presets.get(_cat, []))
        for None in :
            s = None
    
        , [], _new_slots, s = _slots, s
        if not _new_slots != _slots:
            continue
        presets[_cat] = _new_slots
    for None in mega_party_now,:
        if not int(d) != dex:
            continue
    mega_party_now, = , []
    d = self.state.get('mega_party', []), d
    if len(mega_party_now) != len(self.state.get('mega_party', [])):
        self.state['mega_party'] = mega_party_now
    if changed:
    
        try:
            self._rebuild_companions()
            return changed
            return changed
        
        
        
        except Exception:
            return changed
