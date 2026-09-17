# module.PetApp.open_coin_gacha
# source line 12297
# Recovered from bytecode; default argument values are not shown.

def open_coin_gacha(self):
    self._migrate_coin_wallet_to_gold()
    self._ensure_gacha_pool()
    win = None(self.root)
    win.title('🎰 코인뽑기')
    resolve_species_win(win, 480, 430)
    body = None(win)
    body.pack(fill = 'both', expand = True, padx = 12, pady = 10)
    None(body, text = '🎰 코인뽑기', font = ('맑은 고딕', 13, 'bold')).pack(pady = (0, 2))
    None(body, text = f'''1회 {GACHA_PULL_COST}골드 · 하루 {GACHA_MAX_PER_DAY}번 · 한 번 연 칸은 그대로 남아있다가\n100칸을 전부 열면 새 판으로 자동으로 다시 채워져요 (상점과 같은 골드예요)''', font = ('맑은 고딕', 8), fg = '#666', justify = 'center', wraplength = 440).pack(pady = (0, 6))
    info_var = None()
    None(body, textvariable = info_var, font = ('맑은 고딕', 10, 'bold'), fg = '#b8860b').pack(pady = (0, 8))
    main_row = None(body)
    main_row.pack(fill = 'both', expand = True)
    grid_frame = None(main_row)
    grid_frame.pack(side = 'left')
    side_frame = None(main_row, text = '남은 개수', padx = 8, pady = 6)
    side_frame.pack(side = 'left', fill = 'y', padx = (10, 0))
    side_vars = { }
    for None in GACHA_POOL_COMPOSITION:
        amount = ()
        _cnt = None
        v = None()
    tk.StringVar
    cell_btns = []

    def _refresh_side():
        '''coin_gacha_pool'''
        if not self.state.get('coin_gacha_pool'):
            self.state.get('coin_gacha_pool')
        pool = {
            'revealed': [],
            'cells': [] }
        cells = pool.get('cells', [])
        revealed = pool.get('revealed', [])
        for amount, _cnt in GACHA_POOL_COMPOSITION:
            left = (lambda .0: for None in .0:
    c = ()r = Noneif not c == amount:
    continueif r:
    continue1)(zip(cells, revealed)())
            side_vars[amount].set(f'''{amount}골드: 남은 {left}개''')
        info_var.set(f'''💰 보유: {self.state.get('gold', 0)}골드   |   오늘 {self._gacha_today_count()}/{GACHA_MAX_PER_DAY}회 사용''')


    def _refresh_grid():
        '''coin_gacha_pool'''
        if not self.state.get('coin_gacha_pool'):
            self.state.get('coin_gacha_pool')
        pool = {
            'revealed': [],
            'cells': [] }
        cells = pool.get('cells', [])
        revealed = pool.get('revealed', [])
        for None in enumerate(cell_btns):
            i = ()
            btn = None
            if i < len(revealed) and revealed[i]:
                btn.configure(text = f'''{cells[i]}''', state = tk.DISABLED, relief = 'sunken', bg = '#fff6d8')
                continue
        return None
        except Exception:
            continue
        except Exception:
            continue


    def _on_cell_click(idx):
        '''PikaPet'''
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

    for i in range(GACHA_GRID_N * GACHA_GRID_N):
        r = ()
        c = divmod(i, GACHA_GRID_N)
        b.grid(row = r, column = c, padx = 1, pady = 1)
        cell_btns.append(b)
    tk.Button
    None()
    None()
    None(body, text = '닫기', command = win.destroy).pack(pady = (10, 0))
    self._add_opacity_control(win)
