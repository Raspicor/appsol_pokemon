# module.PetApp._buy_myth_token
# source line 13425
# Recovered from bytecode; default argument values are not shown.

def _buy_myth_token(self, refresh_cb):
    locked_reason = self._shop_gen_locked_reason(4)
    if locked_reason:
        None('PikaPet', f'''🔒 아직 살 수 없어요 - {locked_reason}.''')
        return None
    caught = None.state.get('caught', { })
    for None in candidates,:
        if not str(d) not in caught:
            continue
    candidates, = , []
    d = SINNOH_TRIO_DEX, d
    if not candidates:
        None('PikaPet', '축하해요! 디아루가/펄기아/아르세우스를 이미 모두 잡았어요.')
        return None
    cost = None
    gold = int(self.state.get('gold', 0))
    if gold < cost:
        None('PikaPet', f'''골드가 부족해요! (필요: {cost}골드, 보유: {gold}골드)''')
        return None
    if not None('PikaPet', f'''💰{cost}골드로 \'신화 트리오 전용 조우권\'을 구매할까요?\n(디아루가/펄기아/아르세우스 중 하나가 무조건 걸려요)'''):
        return None
    self.state['gold'] = None - None.askyesno
    self.save_state()
    self._open_legend_spin(candidates, 4, refresh_cb)
    return None
