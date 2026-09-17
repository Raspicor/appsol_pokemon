# module.PetApp.open_minigame_hub
# source line 5602
# Recovered from bytecode; default argument values are not shown.

def open_minigame_hub(self):
    win = None(self.root)
    win.title('미니게임')
    resolve_species_win(win, 380, 560)
    self._active_minigame_hub_win = win

    def _on_hub_close():
        '''_active_minigame_hub_win'''
        if getattr(self, '_active_minigame_hub_win', None) is win:
            self._active_minigame_hub_win = None
        win.destroy()

    win.protocol('WM_DELETE_WINDOW', _on_hub_close)
    bottom = None(win)
    bottom.pack(side = 'bottom', pady = 10)
    canvas_holder = None(win)
    canvas_holder.pack(side = 'top', fill = 'both', expand = True, padx = (14, 0))
    hub_canvas = None(canvas_holder, highlightthickness = 0)
    hub_vsb = None(canvas_holder, orient = 'vertical', command = hub_canvas.yview)
    body = None(hub_canvas)
    body.bind('<Configure>', (lambda e: hub_canvas.configure(scrollregion = hub_canvas.bbox('all'))))
    hub_canvas.create_window((0, 0), window = body, anchor = 'nw')
    hub_canvas.configure(yscrollcommand = hub_vsb.set)
    hub_canvas.pack(side = 'left', fill = 'both', expand = True)
    hub_vsb.pack(side = 'right', fill = 'y')

    def _hub_mousewheel(event):
        delta = -1 if event.num == 5 or event.delta < 0 else 1
    
        try:
            if hub_canvas.winfo_exists():
            
                try:
                    hub_canvas.yview_scroll(-delta, 'units')
                    return None
                    return None
                except Exception:
                    return None




    def _bind_hub_wheel(_e = None):
        '''<MouseWheel>'''
        hub_canvas.bind_all('<MouseWheel>', _hub_mousewheel)
        hub_canvas.bind_all('<Button-4>', _hub_mousewheel)
        hub_canvas.bind_all('<Button-5>', _hub_mousewheel)


    def _unbind_hub_wheel(_e = None):
        '''<MouseWheel>'''
        hub_canvas.unbind_all('<MouseWheel>')
        hub_canvas.unbind_all('<Button-4>')
        hub_canvas.unbind_all('<Button-5>')

    hub_canvas.bind('<Enter>', _bind_hub_wheel)
    hub_canvas.bind('<Leave>', _unbind_hub_wheel)
    win.bind('<Destroy>', (lambda e: if e.widget is win:
    None()))
    None(body, text = '🎮 미니게임', font = ('맑은 고딕', 13, 'bold')).pack(pady = (0, 2))
    None(body, text = '연습은 몇 번이든 OK, 도전은 하루 1번! 도전에서 잘하면\n공격력 보너스를 얻어요 (수련의 방 보너스와는 별개로 쌓여요).', font = ('맑은 고딕', 8), fg = '#666', justify = 'left', wraplength = 340).pack(pady = (0, 4))
    None(body, text = f'''🌟 오늘 4개 게임 도전을 전부 마치면 추가로 공격력 +{MINIGAME_ALL_CLEAR_BONUS_PCT:.2f}%!\n   (1등을 다 받으면 하루 최대 +2.00%까지 쌓여요)''', font = ('맑은 고딕', 8, 'bold'), fg = '#8a5a00', justify = 'left', wraplength = 340, relief = 'groove', bd = 1, padx = 6, pady = 4).pack(pady = (0, 10), fill = 'x')
    games = [
        ('feed', '🍎 먹이 받기', '떨어지는 먹이를 제때 클릭해서 받아요.', self.open_game_feed, '🥇배고픔 완전회복+애정도+15\n +조우확률 1.5배(1시간)\n🥈배고픔 완전회복+애정도+10\n🥉배고픔 절반회복+애정도+5\n참가 애정도+2'),
        ('card', '🃏 도감 카드 기억력', '시작 전 카드를 잠깐 보여줘요.\n외워서 같은 짝을 찾아보세요.', self.open_game_memory, '🥇실수 0~1회: 공격력+0.5%\n🥈실수 2~3회: 공격력+0.3%\n🥉실수 4~5회: 공격력+0.15%\n실패: 보상 없음'),
        ('quiz', '❓ 포켓몬 퀴즈', '실루엣과 설명을 보고 어떤\n포켓몬인지 맞혀요.', self.open_game_quiz, '🥇5문제 중 5개: 공격력+0.5%\n🥈4개: 공격력+0.3%\n🥉3개: 공격력+0.15%\n실패(2개 이하): 보상 없음'),
        ('throw', '🎯 몬스터볼 조준', '5번 안에 타이밍 맞춰 클릭해서\n정확도를 겨뤄요.', self.open_game_throw, '🥇5번 모두 성공: 공격력+0.5%\n🥈4번 성공: 공격력+0.3%\n🥉2~3번 성공: 공격력+0.15%\n실패(0~1번): 보상 없음')]
    for None in games:
        key = ()
        title = None
        desc = games
        opener = tk.Label
        left_col.pack(side = 'left', fill = 'both', expand = True, anchor = 'n')
        right_col.pack(side = 'right', anchor = 'n', padx = (6, 0))
        None(left_col, text = title, font = ('맑은 고딕', 10, 'bold')).pack(anchor = 'w')
        None(left_col, text = desc, font = ('맑은 고딕', 8), fg = '#666', justify = 'left', wraplength = 170).pack(anchor = 'w')
        self._minigame_played_today(key) = tk.Label
        status = None(left_col, font = ('맑은 고딕', 8), fg = '#1a4a8a', justify = 'left', wraplength = 170)
        status.pack(anchor = 'w', pady = (2, 4))
        btn_row = None(left_col)
        btn_row.pack(anchor = 'w')
        None(btn_row, text = '연습하기', width = 10, command = (lambda o = opener: None(practice = True))).pack(side = 'left', padx = (0, 6))
        challenge_btn = None(btn_row, text = '도전하기!', width = 10, command = (lambda o = opener: None(practice = False)))
        if played:
            challenge_btn.configure(state = 'disabled')
        challenge_btn.pack(side = 'left')
        None(right_col, text = '🏆 보상', font = ('맑은 고딕', 8, 'bold'), fg = '#333').pack(anchor = 'w')
        None(right_col, text = reward_text, font = ('맑은 고딕', 7), fg = '#555', justify = 'left', wraplength = 140).pack(anchor = 'w')
    tk.Label
    row5 = None(body, relief = 'groove', bd = 1, padx = 8, pady = 6)
    row5.pack(fill = 'x', pady = 4)
    left5 = None(row5)
    left5.pack(side = 'left', fill = 'both', expand = True, anchor = 'n')
    right5 = None(row5)
    right5.pack(side = 'right', anchor = 'n', padx = (6, 0))
    None(left5, text = '⚫ 오목', font = ('맑은 고딕', 10, 'bold')).pack(anchor = 'w')
    None(left5, text = '15x15 판에서 포켓몬 얼굴 돌로 오목을 둬요.\n1인(AI 난이도 5단계) 또는 2인이서 즐겨요.', font = ('맑은 고딕', 8), fg = '#666', justify = 'left', wraplength = 170).pack(anchor = 'w')
    None(left5, text = '오목 두기', width = 10, command = self.open_game_omok).pack(anchor = 'w', pady = (4, 0))
    None(right5, text = '🎲 (보상없음)', font = ('맑은 고딕', 8, 'bold'), fg = '#333').pack(anchor = 'w')
    None(right5, text = '그냥 재미로\n즐기는 게임이에요', font = ('맑은 고딕', 7), fg = '#555', justify = 'left', wraplength = 140).pack(anchor = 'w')
    None(bottom, text = '닫기', command = _on_hub_close).pack()
    self._add_opacity_control(win)
