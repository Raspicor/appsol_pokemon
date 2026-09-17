# module.PetApp.open_pokedex._equip_selected
# source line 16328
# Recovered from bytecode; default argument values are not shown.

def _equip_selected():
    d = selected['dex']
    if d is not None or selected['status'] != 'caught':
        None('PikaPet', '아직 잡지 못한 포켓몬은 장착할 수 없어요.')
        return None
    if set in (lambda .0: for x in .0:
    int(x).0)(self.state.get('sacrificed', [])()):
        None('PikaPet', '메가진화 재물로 이미 바친 포켓몬이라 장착할 수 없어요.')
        return None
    if None._dex_is_taken_by_body(d):
        None('PikaPet', '지금 본체(또는 2번 본체)로 쓰고 있는 포켓몬이에요. 이미 그\n능력치를 그대로 받고 있어서, 동료로 또 장착하면 중복이라\n넣을 수 없어요.')
        return None
    if None(d)['mode'] != 'default':
        None(d, mode_box['mode'])
        return None
    cap = None(self.state)
    party = self.state.get('party', [])
    if d in party:
        None('PikaPet', '이미 장착돼 있어요.')
        return None
    if None(party) >= cap:
        None('PikaPet', f'''지금은 동료를 {cap}칸까지만 장착할 수 있어요.\n먼저 다른 동료를 해제하거나, 포켓몬을 더 잡아 레벨을 올려보세요.''')
        return None
    if None(party) == 0:
        party = list(party)
        party.append(d)
        self.state['party'] = party
        self._rebuild_companions()
        self.save_state()
        None()
        return None
    None(d)
