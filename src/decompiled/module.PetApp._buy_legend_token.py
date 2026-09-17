# module.PetApp._buy_legend_token
# source line 13451
# Recovered from bytecode; default argument values are not shown.

def _buy_legend_token(self, gen, refresh_cb):
    locked_reason = self._shop_gen_locked_reason(gen)
    if locked_reason:
        None('PikaPet', f'''🔒 아직 살 수 없어요 - {locked_reason}.''')
        return None
    caught = None.state.get('caught', { })
    lo = ()
    hi = gen_dex_range(gen)
    for None in :
        d = ()
        e = None
        if not e.get('legendary'):
            continue
        if  <= lo, d:
            if not lo, d < hi:
                continue
            else:
            
            if not str(d) not in caught:
                continue

    , [], candidates, d = POKEDEX.items(), d, e
    e = None
    if not candidates:
        None('PikaPet', f'''축하해요! {gen}세대 전설 포켓몬을 이미 모두 잡았어요. 토큰을 살 필요가 없어요.''')
        return None
    cost = None._token_cost(gen)
    gold = int(self.state.get('gold', 0))
    if gold < cost:
        None('PikaPet', f'''골드가 부족해요! (필요: {cost}골드, 보유: {gold}골드)''')
        return None
    if not None('PikaPet', f'''💰{cost}골드로 \'{gen}세대 전설조우 토큰\'을 구매할까요?\n(사는 즉시 어떤 전설이 걸릴지 회오리 뽑기로 정해져요)'''):
        return None
    self.state['gold'] = None - None.askyesno
    self.save_state()
    self._open_legend_spin(candidates, gen, refresh_cb)
    return None
