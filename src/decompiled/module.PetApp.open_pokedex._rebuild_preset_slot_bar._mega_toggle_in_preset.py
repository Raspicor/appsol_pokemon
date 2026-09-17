# module.PetApp.open_pokedex._rebuild_preset_slot_bar._mega_toggle_in_preset
# source line 16459
# Recovered from bytecode; default argument values are not shown.

def _mega_toggle_in_preset(d):
    if not mega_companion_ready(d, self.state.get('caught', { })):
        None('PikaPet', f'''이 동료는 메가진화 대상 종이 아니거나, 아직 최고 레벨(Lv.{MAX_PLAYER_LEVEL})로\n잡지 못했어요. 최고 레벨 개체를 잡아서 켜보세요.''')
        return None
    mp = (lambda .0: for x in .0:
    int(x).0)(self.state.get('mega_party', [])())
    if int(d) in mp:
        mp.discard(int(d))
    else:
        mp.add(int(d))
    self.state['mega_party'] = list(mp)
    self._rebuild_companions()
    self.save_state()
    None()
