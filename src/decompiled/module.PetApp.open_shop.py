# module.PetApp.open_shop
# source line 13132
# Recovered from bytecode; default argument values are not shown.

def open_shop(self):
    WIN_W = 340
    CONTENT_W = WIN_W - 36
    win = None(self.root)
    win.title('🏪 상점')
    resolve_species_win(win, WIN_W, 560)
    win.resizable(True, True)

    try:
        win.geometry(f'''{WIN_W}x560''')
        win.minsize(260, 300)
    
        try:
            win.attributes('-topmost', True)
            outer_canvas = None(win, highlightthickness = 0, width = WIN_W - 18)
            vscroll = None(win, orient = 'vertical', command = outer_canvas.yview)
            outer_canvas.configure(yscrollcommand = vscroll.set)
            outer_canvas.pack(side = 'left', fill = 'both', expand = True)
            vscroll.pack(side = 'right', fill = 'y')
            outer = None(outer_canvas)
            win_id = outer_canvas.create_window((0, 0), window = outer, anchor = 'nw', width = WIN_W - 18)
        
            def _on_outer_configure(evt = None):
                '''all'''
                outer_canvas.configure(scrollregion = outer_canvas.bbox('all'))

            outer.bind('<Configure>', _on_outer_configure)
        
            def _on_canvas_configure(evt):
            
                try:
                    outer_canvas.itemconfig(win_id, width = evt.width)
                    return None
                except Exception:
                    return None


            outer_canvas.bind('<Configure>', _on_canvas_configure)
        
            def _shop_wheel(event):
                '''num'''
                delta = -1 if getattr(event, 'num', 0) == 5 or event.delta < 0 else 1
            
                try:
                    if outer_canvas.winfo_exists():
                    
                        try:
                            outer_canvas.yview_scroll(-delta, 'units')
                            return None
                            return None
                        except Exception:
                            return None



        
            def _bind_shop_wheel(_e = None):
                '''<MouseWheel>'''
                outer_canvas.bind_all('<MouseWheel>', _shop_wheel)
                outer_canvas.bind_all('<Button-4>', _shop_wheel)
                outer_canvas.bind_all('<Button-5>', _shop_wheel)

        
            def _unbind_shop_wheel(_e = None):
                '''<MouseWheel>'''
                outer_canvas.unbind_all('<MouseWheel>')
                outer_canvas.unbind_all('<Button-4>')
                outer_canvas.unbind_all('<Button-5>')

            outer_canvas.bind('<Enter>', _bind_shop_wheel)
            outer_canvas.bind('<Leave>', _unbind_shop_wheel)
            outer_canvas.bind('<Destroy>', _unbind_shop_wheel, add = '+')
            gold_var = None()
            None(outer, textvariable = gold_var, font = ('맑은 고딕', 13, 'bold'), fg = '#b8860b').pack(pady = (14, 2))
            None(outer, text = '포켓몬을 잡을 때마다(중복 포획 포함) 10골드씩 쌓여요.', font = ('맑은 고딕', 8), fg = '#777', wraplength = CONTENT_W).pack(pady = (0, 10))
            gen_labels = {
                4: '4세대',
                3: '3세대',
                2: '2세대',
                1: '1세대' }
            gacha_btns = { }
            token_btns = { }
            for gen in (1, 2, 3, 4):
                box = None(outer, text = f'''◆ {gen_labels[gen]}''', padx = 10, pady = 8)
                box.pack(fill = 'x', padx = 12, pady = 6)
                None(box, text = f'''랜덤 뽑기 - 도감에 없는 {gen_labels[gen]} 포켓몬 중 랜덤(전설 제외). 능력치/레벨도 랜덤으로 정해져서 바로 도감에 등록돼요.''', font = ('맑은 고딕', 8), fg = '#555', justify = 'left', wraplength = CONTENT_W - 20).pack(anchor = 'w', fill = 'x')
                gbtn = None(box, command = (lambda g = gen: (_refresh, None())), wraplength = CONTENT_W - 30, justify = 'center')
                gbtn.pack(fill = 'x', pady = (4, 8))
                gacha_btns[gen] = gbtn
                None(box, text = '전설조우 토큰 - 사는 순간 회오리 뽑기로 어떤 전설이 걸릴지 하나로 확정되고, 그 전설 하나에게만 총 3번 도전할 수 있어요(잡는 순간 남은 횟수는 바로 사라져요).', font = ('맑은 고딕', 8), fg = '#555', justify = 'left', wraplength = CONTENT_W - 20).pack(anchor = 'w', fill = 'x')
                tbtn = None(box, command = (lambda g = gen: self._buy_legend_token(g, _refresh)), wraplength = CONTENT_W - 30, justify = 'center')
                tbtn.pack(fill = 'x', pady = (4, 0))
                token_btns[gen] = tbtn
            tk.Label
            ticket_box = None(outer, text = '◆ 전설 선택권 (무한성장미터 보상)', padx = 10, pady = 8)
            ticket_box.pack(fill = 'x', padx = 12, pady = 6)
            None(ticket_box, text = '무한성장미터에서 100단위 스테이지(거울대결)를 깨면 받는 티켓이에요. 쓰는 순간 그 세대 전설 중 하나를 직접 골라서 Lv.5로 바로 받아요.', font = ('맑은 고딕', 8), fg = '#555', justify = 'left', wraplength = CONTENT_W - 20).pack(anchor = 'w')
            ticket_btns = { }
            for gen in (1, 2, 3, 4):
                tkbtn = None(ticket_box, command = (lambda g = gen: (_refresh, None())), wraplength = CONTENT_W - 30, justify = 'center')
                tkbtn.pack(fill = 'x', pady = (4, 0))
                ticket_btns[gen] = tkbtn
            (1, 2, 3, 4)
            myth_box = None(outer, text = '◆ 4세대 신화 트리오 전용 조우권', padx = 10, pady = 8)
            myth_box.pack(fill = 'x', padx = 12, pady = 6)
            None(myth_box, text = '디아루가/펄기아/아르세우스 중 하나가 무조건 걸려요(이미 잡은 건 후보에서 빠짐). 일반 4세대 토큰과 같은 자리를 쓰기 때문에, 진행 중인 토큰이 있어도 또 살 수 있어요(같은 전설이면 도전 횟수가 쌓이고, 다른 전설이면 그쪽으로 바뀌어요).', font = ('맑은 고딕', 8), fg = '#555', justify = 'left', wraplength = CONTENT_W - 20).pack(anchor = 'w')
            myth_btn = None(myth_box, command = (lambda : (_refresh, None())), wraplength = CONTENT_W - 30, justify = 'center')
            myth_btn.pack(fill = 'x', pady = (4, 0))
            item_box = None(outer, text = '◆ 아이템', padx = 10, pady = 8)
            item_box.pack(fill = 'x', padx = 12, pady = 6)
            None(item_box, text = f'''🍎 포켓몬 먹이 - 30분 동안 야생 포켓몬 조우 확률이 2배가 돼요. (하루 최대 {POKEMON_FOOD_DAILY_LIMIT}번까지)''', font = ('맑은 고딕', 8), fg = '#555', justify = 'left', wraplength = CONTENT_W - 20).pack(anchor = 'w')
            food_btn = None(item_box, command = (lambda : (_refresh, None())), wraplength = CONTENT_W - 30, justify = 'center')
            food_btn.pack(fill = 'x', pady = (4, 0))
        
            def _refresh():
                '''💰 보유 골드: '''
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
            
            
            
            

            None(outer, text = '닫기', command = win.destroy).pack(pady = (14, 14))
            self._add_opacity_control(win)
            None()
            _food_tick_state = {
                'was_active': False }
        
            def _food_tick():
            
                try:
                    if not win.winfo_exists():
                        return None
                    bl = time.time - None()
                    if bl > 0:
                        _food_tick_state['was_active'] = True
                        blt = int(bl)
                        mm = ()
                        ss = divmod(blt, 60)
                    
                        try:
                            food_btn.configure(text = f'''🍎 사용 중! (조우확률 2배, {mm}분 {ss:02d}초 남음)''')
                        if _food_tick_state['was_active']:
                            None()

                    win.after(1000, _food_tick)
                    return None
                except Exception:
                    return None
                    except Exception:
                        continue


            win.after(1000, _food_tick)
            return None
            except Exception:
                tk.Button
                continue
        except Exception:
            continue
