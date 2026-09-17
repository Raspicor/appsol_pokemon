# module.PetApp.open_pokedex._bulk_lock
# source line 15786
# Recovered from bytecode; default argument values are not shown.

def _bulk_lock(lock_on):
    caught_dex = (lambda .0: for d in .0:
    int(d).0)(self.state.get('caught', { }).keys()())
    pinned = self.starter_stage_conf().get('dex')
    if pinned is not None:
        caught_dex.add(int(pinned))
    if lock_on:
        if not caught_dex:
            None('PikaPet', '아직 보유 중인 포켓몬이 없어요.')
            return None
        if not None('PikaPet', f'''지금 보유 중인 포켓몬 {len(caught_dex)}마리를 전부 잠글까요?'''):
            return None
        self.state['party_locked'] = set.askyesno(caught_dex)
    elif not None('PikaPet', '잠긴 포켓몬을 전부 해제할까요?'):
        return None
    self.state['party_locked'] = []
    self.save_state()
    None()
