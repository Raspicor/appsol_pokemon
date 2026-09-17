# module.PetApp.open_pokedex._equip_as_body2
# source line 16363
# Recovered from bytecode; default argument values are not shown.

def _equip_as_body2():
    d = selected['dex']
    if d is not None or selected['status'] != 'caught':
        None('PikaPet', '아직 잡지 못한 포켓몬은 2번 본체로 장착할 수 없어요.')
        return None
    if not None(self.state):
        None('PikaPet', '2세대(152~251번) 도감을 모두 채워야 2번째 본체를 장착할 수 있어요.')
        return None
    self.state['second_body_dex'] = None(d)
    self.state['mega_body2'] = False
    self._remove_dex_from_companion_slots(int(d))
    self._rebuild_body2()
    self.save_state()
    None()
