# module.PetApp.open_coin_gacha._on_cell_click
# source line 12359
# Recovered from bytecode; default argument values are not shown.

def _on_cell_click(idx):
    if self._gacha_today_count() >= GACHA_MAX_PER_DAY:
        None('PikaPet', f'''오늘 코인뽑기는 다 쓰셨어요! (하루 {GACHA_MAX_PER_DAY}번)\n내일 다시 와주세요.''')
        return None
    pool = None.state.get('coin_gacha_pool')
    if pool and idx >= len(pool.get('revealed', [])) or pool['revealed'][idx]:
        return None
    wallet = None.state.get('gold', 0)
    if wallet < GACHA_PULL_COST:
        None('PikaPet', f'''골드가 부족해요! (필요: {GACHA_PULL_COST}골드, 보유: {wallet}골드)\n⛏ 광산에서 골드를 더 모아오세요!''')
        return None
    pool['revealed'][idx] = None
    reward = pool['cells'][idx]
    self.state['gold'] = wallet - GACHA_PULL_COST
    self._earn_gold(reward)
    self._gacha_bump_today()
    self.save_state()
    None()
    None()
    net = reward - GACHA_PULL_COST
    sign = '+' if net >= 0 else ''
    None('코인뽑기 결과', f'''🪙 {reward}골드가 나왔어요! (이번 뽑기 손익: {sign}{net}골드)''')
    if all(pool['revealed']):
        self.state['coin_gacha_pool'] = self._new_gacha_pool()
        self.save_state()
        None()
        None()
        None('PikaPet', '🎉 100칸을 모두 여셨어요! 새로운 뽑기판으로 다시 채워졌어요.')
        return None
    return messagebox.showinfo
