# module.PetApp.open_pokedex._swap_body
# source line 16381
# Recovered from bytecode; default argument values are not shown.

def _swap_body():
    d = selected['dex']
    if d is not None or selected['status'] != 'caught':
        None('PikaPet', '아직 잡지 못한 포켓몬은 본체로 쓸 수 없어요.')
        return None
    if not None(self.state):
        None('PikaPet', '본체 교체는 원래 스타터 포켓몬이 레벨 5 이상 + 1회 이상\n진화해야 열려요.')
        return None
    if not self.state.get('custom_body_dex'):
        self.state.get('custom_body_dex')
    if None(d) == int(-1):
        None('PikaPet', '이미 이 포켓몬이 본체예요.')
        return None
    if not None('PikaPet', f'''본체를 {POKEDEX.get(d, { }).get('kr', '?')}(으)로 교체할까요?\n(원래 스타터는 도감 목록 위쪽에 🌟스타터로 고정 표시되고,\n진행도도 그대로 남아있어서 언제든 되돌릴 수 있어요)'''):
        return None
    None.askyesno.set_custom_body(d)
    None()
