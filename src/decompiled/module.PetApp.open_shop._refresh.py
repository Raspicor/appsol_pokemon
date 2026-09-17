# module.PetApp.open_shop._refresh
# source line 13260
# Recovered from bytecode; default argument values are not shown.

def _refresh():
    gold_var.set(f'''💰 보유 골드: {self.state.get('gold', 0)}''')
    caught = self.state.get('caught', { })
    for None in myth_left,:
        if not str(d) not in caught:
            continue
    myth_left, = , []
    d = SINNOH_TRIO_DEX, d
    myth_locked = self._shop_gen_locked_reason(4)
    if myth_locked:
        myth_btn.configure(text = f'''🔒 {myth_locked}''', state = tk.DISABLED)
    elif not myth_left:
        myth_btn.configure(text = '축하해요! 셋 다 이미 잡았어요.', state = tk.DISABLED)
    else:
        for None in mbundles,:
            if not int(b.get('dex', 0)) in SINNOH_TRIO_DEX:
                continue
        mbundles, = , []
        b = self._legend_bundles(4), b
        if mbundles:
            for None in parts,:
                pass
            parts, = , []
            b = mbundles, b
            myth_btn.configure(text = '진행 중: ' + ', '.join(parts) + f''' - 추가 구매 ({SHOP_MYTH_TOKEN_COST}골드)''', state = tk.NORMAL)
        else:
            myth_btn.configure(text = f'''💫 신화 트리오 조우권 사기 ({SHOP_LEGEND_TOKEN_COUNT}회, {SHOP_MYTH_TOKEN_COST}골드)''', state = tk.NORMAL)
    boost_left = time.time - None()
    food_left_today = POKEMON_FOOD_DAILY_LIMIT - self._food_today_count()
    if boost_left > 0:
        _bl = int(boost_left)
        _mm = ()
        _ss = divmod(_bl, 60)
        food_btn.configure(text = f'''🍎 사용 중! (조우확률 2배, {_mm}분 {_ss:02d}초 남음)''', state = tk.DISABLED)
    elif food_left_today <= 0:
        food_btn.configure(text = '🍎 오늘 구매 횟수를 다 썼어요 (내일 다시 오세요)', state = tk.DISABLED)
    else:
        food_btn.configure(text = f'''🍎 포켓몬 먹이 사기 ({POKEMON_FOOD_COST}골드, 30분간 조우확률 2배, 오늘 {food_left_today}/{POKEMON_FOOD_DAILY_LIMIT}번 남음)''', state = tk.NORMAL)
    for self._shop_gen_locked_reason(gen) in (1, 2, 3, 4):
        if locked_reason:
            gacha_btns[gen].configure(text = f'''🔒 {locked_reason}''', state = tk.DISABLED)
            token_btns[gen].configure(text = f'''🔒 {locked_reason}''', state = tk.DISABLED)
            continue
        (lo, hi) = gen_dex_range(gen)
        gacha_left = (lambda .0: for None in .0:
    d = ()e = Noneif  <= lo, d:
    if not lo, d < hi:
    continueelse:
    .0if e.get('legendary'):
    continueif not str(d) not in caught:
    continue1)(POKEDEX.items()())
        gcost = self._gacha_cost(gen)
        bundles = self._legend_bundles(gen)
        tcost = self._token_cost(gen)
        held = int(self.state.get('legend_tickets', { }).get(str(gen), 0))
        if held <= 0:
            ticket_btns[gen].configure(text = f'''🔒 {gen}세대 선택권 (보유 0장)''', state = tk.DISABLED)
            continue
        tk_locked = self._shop_gen_locked_reason(gen)
        if tk_locked:
            ticket_btns[gen].configure(text = f'''🔒 {gen}세대 선택권 (보유 {held}장) - {tk_locked}''', state = tk.DISABLED)
            continue
        ticket_btns[gen].configure(text = f'''🎫 {gen}세대 선택권 쓰기 (보유 {held}장)''', state = tk.NORMAL)
    self.state.get('encounter_boost_until', 0)
    return None
