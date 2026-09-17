# module.PetApp.open_game_quiz
# source line 6184
# Recovered from bytecode; default argument values are not shown.

def open_game_quiz(self, practice):
    if practice and self._minigame_played_today('quiz'):
        None('PikaPet', "오늘은 이미 '포켓몬 퀴즈' 도전을 마쳤어요. 내일 다시 도전해보세요!\n(연습하기는 계속 하실 수 있어요.)")
        return None
    if None._minigame_window_active():
        None('PikaPet', '이미 다른 미니게임 창이 열려 있어요! 먼저 그 창을 닫아주세요.')
        return None
    caught_dex = (lambda .0: for d in .0:
    int(d).0)(self.state.get('caught', { }).keys()())
    if len(caught_dex) < 1:
        None('PikaPet', '아직 잡은 포켓몬이 없어서 퀴즈를 낼 수 없어요!\n야생 포켓몬을 먼저 잡아보세요.')
        return None
    all_dex = None(POKEDEX.keys())
    if len(all_dex) < 4:
        None('PikaPet', '도감 데이터가 부족해서 퀴즈를 열 수 없어요.')
        return None
    if not None:
        self._warn_challenge_start()
    win = None(self.root)
    win.title('포켓몬 퀴즈' + ' (연습)' if practice else ' (도전!)')
    resolve_species_win(win, 360, 460)
    self._active_minigame_win = win
    if not practice:
        self._mark_minigame_started('quiz')
    win.images = []
    rounds = 5
    time_limit = 8
    pool = list(caught_dex)
    None(pool)
    quiz_dex = []
    if len(quiz_dex) < rounds:
        quiz_dex.extend(pool)
        continue
    quiz_dex = quiz_dex[:rounds]
    ctx = {
        'current_correct_dex': None,
        'remaining': time_limit,
        'answered': False,
        'correct': 0,
        'round': 0,
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
    None(win, text = '❓ 이 실루엣과 설명은 어떤 포켓몬일까요?', font = ('맑은 고딕', 10, 'bold')).pack(pady = (10, 2))
    sil_label = None(win)
    sil_label.pack(pady = (2, 2))
    status_var = None(value = '')
    None(win, textvariable = status_var, font = ('맑은 고딕', 9), fg = '#555').pack(pady = (0, 2))
    timer_var = None(value = '')
    None(win, textvariable = timer_var, font = ('맑은 고딕', 9, 'bold'), fg = '#c0392b').pack()
    question_var = None(value = '')
    None(win, textvariable = question_var, font = ('맑은 고딕', 10), wraplength = 320, justify = 'left', fg = '#222').pack(padx = 12, pady = (8, 10))
    btns_frame = None(win)
    btns_frame.pack(pady = 4)

    def _tick_timer():
        '''closed'''
        if ctx['closed'] or ctx['answered']:
            return None
        if ctx['remaining'] <= 0:
            timer_var.set('시간 초과!')
            None(None)
            return None
        None.set(f'''남은 시간: {ctx['remaining']}초''')
        win.after(1000, _tick_timer) = None


    def _answer(chosen_dex):
        '''closed'''
        if ctx['closed'] or ctx['answered']:
            return None
        ctx['answered'] = None
        None()
        reveal_img = self._sprite_preview_image(ctx['current_correct_dex'], size = 90)
        win.images.append(reveal_img)
        sil_label.configure(image = reveal_img)
        if chosen_dex == ctx['current_correct_dex']:
            timer_var.set('정답!')
        else:
            POKEDEX.get(ctx['current_correct_dex'], { }).get('kr', '?') = _cancel
            timer_var.set(f'''오답! 정답은 \'{correct_name}\'''')
        for w in btns_frame.winfo_children():
            w.configure(state = 'disabled')
        win.after(900, _new_round)
        return None
        except Exception:
            continue


    def _new_round():
        '''closed'''
        if ctx['closed']:
            return None
        if None['round'] >= rounds:
            None()
            return None
        idx = None['round']
        quiz_dex[idx] = None
        entry = POKEDEX.get(dex, { })
        correct_name = entry.get('kr', f'''#{dex}''')
        if not entry.get('desc'):
            entry.get('desc')
        desc = ''
        elem = entry.get('element', '')
        clue = desc if desc else f'''타입: {elem}'''
        question_var.set(f'''[{ctx['round']}/{rounds}번] {clue}''')
        status_var.set(f'''맞힌 개수: {ctx['correct']}개''')
        sil_img = self._sprite_preview_image(dex, size = 90, silhouette = True)
        win.images.append(sil_img)
        sil_label.configure(image = sil_img)
        for None in :
            d = None
            if not d != dex:
                continue
    
        , [], wrong_pool, d = all_dex, d
        None(wrong_pool)
        wrong_dex = wrong_pool[<TYPE: 58>
    ]
        for None in :
            d = None
    
        wrong_dex, d, , [] + d, = [
            (dex, correct_name)]
        None(options)
        for w in btns_frame.winfo_children():
            w.destroy()
        random.shuffle
        ctx['answered'] = False
        ctx['remaining'] = time_limit
        ctx['current_correct_dex'] = dex
        timer_var.set(f'''남은 시간: {time_limit}초''')
        for None in options:
            opt_dex = ()
            opt_name = None
        options
        None()
        return None
    
    


    def _finish():
        '''correct'''
        None()
        correct = ctx['correct']
        if correct >= 5:
            tier = 'gold'
        elif correct >= 4:
            tier = 'silver'
        elif correct >= 3:
            tier = 'bronze'
        else:
            tier = 'fail'
        for w in btns_frame.winfo_children():
            w.destroy()
        _cancel
        question_var.set(f'''결과: {rounds}문제 중 {correct}개 정답!''')
        timer_var.set(self._minigame_tier_label(tier))
        result_lines = [
            f'''결과: {rounds}문제 중 {correct}개 정답!''',
            self._minigame_tier_label(tier)]
        if practice:
            self._show_minigame_result_popup(win, True, result_lines + [
                '(연습이라 보상은 없어요)'], close_fn = _on_close, retry_fn = (lambda : self.open_game_quiz(practice = True)))
            return None
        msgs = None._minigame_claim('quiz', tier)
        self._refresh_minigame_hub()
        self._show_minigame_result_popup(win, False, result_lines + msgs, close_fn = _on_close)

    None()
