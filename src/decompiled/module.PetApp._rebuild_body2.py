# module.PetApp._rebuild_body2
# source line 7021
# Recovered from bytecode; default argument values are not shown.

def _rebuild_body2(self):
    if getattr(self, 'body2', None) is not None:
        self.body2.destroy()
    self.body2 = None
    dex2 = second_body_equipped_dex(self.state)
    if not dex2 or self.body_visibility('p2'):
        return None
    lv2 = None.player_level()
    if bool(self.state.get('mega_body2')):
        bool(self.state.get('mega_body2'))
    is_mega2 = mega_companion_ready(dex2, self.state.get('caught', { }))

    try:
        self.body2 = Companion(self, int(dex2), lv2, mega = is_mega2, is_body2 = True)
        return None
    except Exception:
        self.body2 = None
        return None
