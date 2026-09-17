# module.PetApp.open_game_memory
# source line 6024
# Recovered from bytecode; default argument values are not shown.

def open_game_memory(self, practice):
    if practice and self._minigame_played_today('card'):
        None('PikaPet', "오늘은 이미 '카드 기억력' 도전을 마쳤어요. 내일 다시 도전해보세요!\n(연습하기는 계속 하실 수 있어요.)")
        return None
    if None._minigame_window_active():
        None('PikaPet', '이미 다른 미니게임 창이 열려 있어요! 먼저 그 창을 닫아주세요.')
        return None
    if not None:
        self._warn_challenge_start()
    for None in :
        d = ()
        e = None
        if not self._has_sprite_art(e):
            continue

    , [], all_dex, d = POKEDEX.items(), d, e
    e = None
    if len(all_dex) < 4:
        None('PikaPet', '도감 데이터가 부족해서 카드 게임을 열 수 없어요.')
        return None
    win = None(self.root)
    win.title('도감 카드 기억력' + ' (연습)' if practice else ' (도전!)')
    resolve_species_win(win, 340, 400)
    self._active_minigame_win = win
    win.images = []
    if not practice:
        self._mark_minigame_started('card')
    PREVIEW_SECONDS = 3
    pair_dex = None(all_dex, 4)
    deck = pair_dex * 2
    None(deck)
    CARD_SIZE = 48
    back_img = self._sprite_card_image(None, size = CARD_SIZE)
    win.images.append(back_img)
    front_imgs = { }
    for d in pair_dex:
        img = self._sprite_card_image(d, size = CARD_SIZE)
        win.images.append(img)
        front_imgs[d] = img
    random.shuffle
    ctx = {
        'preview_remaining': PREVIEW_SECONDS,
        'preview': True,
        'buttons': { },
        'locked': False,
        'mistakes': 0,
        'matched': set(),
        'revealed': [],
        'job': None,
        'closed': False }

    def _cancel():
        '''job'''
        if ctx['job'] is not None:
        
            try:
                win.after_cancel(ctx['job'])
                ctx['job'] = None
                return None
                return None
            except Exception:
                continue



    def _on_close():
        ctx['closed'] = True
        None()
        self._clear_active_minigame_win(win)
        win.destroy()

    win.protocol('WM_DELETE_WINDOW', _on_close)
    self._add_opacity_control(win)
    None(win, text = '🃏 같은 포켓몬 카드 두 장을 찾아 짝지어주세요! (아직 못 잡은 포켓몬도 나와요)', font = ('맑은 고딕', 10, 'bold'), wraplength = 300, justify = 'center').pack(pady = (10, 2))
    status_var = None(value = f'''카드를 잘 기억하세요! {PREVIEW_SECONDS}초 후 시작...''')
    None(win, textvariable = status_var, font = ('맑은 고딕', 9), fg = '#555').pack(pady = (0, 6))
    grid = None(win)
    grid.pack(pady = 4)

    def _finish():
        '''mistakes'''
        mistakes = ctx['mistakes']
        if mistakes <= 1:
            tier = 'gold'
        elif mistakes <= 3:
            tier = 'silver'
        elif mistakes <= 5:
            tier = 'bronze'
        else:
            tier = 'fail'
        result_lines = [
            f'''클리어! 실수 {mistakes}회''',
            self._minigame_tier_label(tier)]
        if practice:
            self._show_minigame_result_popup(win, True, result_lines + [
                '(연습이라 보상은 없어요)'], close_fn = _on_close, retry_fn = (lambda : self.open_game_memory(practice = True)))
            return None
        msgs = None._minigame_claim('card', tier)
        self._refresh_minigame_hub()
        self._show_minigame_result_popup(win, False, result_lines + msgs, close_fn = _on_close)


    def _check_pair():
        '''closed'''
        if ctx['closed']:
            return None
        if None(ctx['revealed']) != 2:
            return None
        (i1, i2) = None['revealed']
        if deck[i1] == deck[i2]:
            ctx['matched'].add(i1)
            ctx['matched'].add(i2)
            ctx['revealed'] = []
            ctx['locked'] = False
            if len(ctx['matched']) == len(deck):
                None()
                return None
            return None
        status_var.set(f'''실수 {ctx['mistakes']}회''')
        (lambda : if ctx['closed']:
    Nonefor idx in (None, i2):
    btn = ctx['buttons'].get(idx)if btn is None:
    continuebtn.configure(image = back_img)ctx['revealed'] = []ctx['locked'] = FalseNoneexcept Exception:
    continue) = None
        win.after(700, _hide_back)


    def _on_card_click(idx):
        '''closed'''
        if ctx['closed'] and ctx['locked'] or ctx['preview']:
            return None
        if None in ctx['matched'] or idx in ctx['revealed']:
            return None
        None['buttons'][idx].configure(image = front_imgs[deck[idx]])
        ctx['revealed'].append(idx)
        if len(ctx['revealed']) == 2:
            ctx['locked'] = True
            win.after(400, _check_pair)
            return None


    def _preview_tick():
        '''closed'''
        if ctx['closed']:
            return None
        if None['preview_remaining'] <= 0:
            ctx['preview'] = False
            for btn in ctx['buttons'].values():
                btn.configure(image = back_img)
            status_var.set('실수 0회 · 이제 같은 카드를 찾아보세요!')
            return None
        None.set(f'''카드를 잘 기억하세요! {ctx['preview_remaining']}초 후 시작...''')
        win.after(1000, _preview_tick) = None
        return None
        except Exception:
            continue

    for i in range(8):
        r = ()
        c = divmod(i, 4)
        b.grid(row = r, column = c, padx = 4, pady = 4)
        b = None(grid, image = front_imgs[deck[i]], command = (lambda idx = i: None(idx)))
    range(8)
    None()
    return None
