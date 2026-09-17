# module.PetApp.open_training_room
# source line 15501
# Recovered from bytecode; default argument values are not shown.

def open_training_room(self):
    win = None(self.root)
    win.title('수련의 방')
    resolve_species_win(win, 340, 480)
    self._active_training_win = win

    def _on_train_win_destroy(_e = None):
        '''_active_training_win'''
        if getattr(self, '_active_training_win', None) is win:
            self._active_training_win = None
            return None

    win.bind('<Destroy>', _on_train_win_destroy)
    bottom = None(win)
    bottom.pack(side = 'bottom', fill = 'x', pady = 8)
    body_outer = None(win)
    body_outer.pack(side = 'top', fill = 'both', expand = True)
    body_canvas = None(body_outer, highlightthickness = 0)
    body_vscroll = None(body_outer, orient = 'vertical', command = body_canvas.yview)
    body_canvas.configure(yscrollcommand = body_vscroll.set)
    body_canvas.pack(side = 'left', fill = 'both', expand = True)
    body_vscroll.pack(side = 'left', fill = 'y')
    body = None(body_canvas)
    _body_win_id = body_canvas.create_window((0, 0), window = body, anchor = 'nw')

    def _on_body_configure(evt = None):
        '''all'''
        body_canvas.configure(scrollregion = body_canvas.bbox('all'))
    
        try:
            body_canvas.itemconfigure(_body_win_id, width = body_canvas.winfo_width())
            return None
        except Exception:
            return None


    body.bind('<Configure>', _on_body_configure)
    body_canvas.bind('<Configure>', _on_body_configure)

    def _body_wheel_scroll(e):
    
        try:
            if body_canvas.winfo_exists():
            
                try:
                    body_canvas.yview_scroll(int(-1 * (e.delta / 120)), 'units')
                    return None
                    return None
                except Exception:
                    return None




    def _bind_body_wheel(evt):
        '''<MouseWheel>'''
        body_canvas.bind_all('<MouseWheel>', _body_wheel_scroll)


    def _unbind_body_wheel(evt = None):
        '''<MouseWheel>'''
        body_canvas.unbind_all('<MouseWheel>')

    body_canvas.bind('<Enter>', _bind_body_wheel)
    body_canvas.bind('<Leave>', _unbind_body_wheel)
    body_canvas.bind('<Destroy>', _unbind_body_wheel, add = '+')
    body_pad = None(body, padx = 16, pady = 16)
    body_pad.pack(fill = 'both', expand = True)
    body = body_pad
    None(body, text = '🏋 수련의 방', font = ('맑은 고딕', 13, 'bold')).pack(pady = (0, 6))
    None(body, text = '1시간(실제 시간)씩 훈련하면 공격력이 영구히 1%씩 올라가요.\n하루 최대 5번까지, 이 보너스는 진화해도 그대로 유지돼요.', font = ('맑은 고딕', 9), fg = '#555', justify = 'left', wraplength = 300).pack(pady = (0, 10))
    bonus_var = None()
    status_var = None()
    action_btn = None(body, width = 20)
    action_btn.pack(pady = 8)

    def refresh():
        '''누적 공격력 보너스: +'''
        bonus_var.set(f'''누적 공격력 보너스: +{self.train_bonus_pct():.1f}%''')
        today_n = self._train_today_count()
        start = self.state.get('train_session_start', 0)
        if start:
            elapsed = None() - start
            remain = max(0, TRAIN_SESSION_SECONDS - elapsed)
            if remain <= 0:
                status_var.set('훈련 완료! 아래 버튼으로 보상을 받으세요.')
                action_btn.configure(text = '🎁 보상 받기 (+1%)', state = 'normal', command = claim)
                return None
            mm = time.time(remain // 60)
            ss = int(remain % 60)
            status_var.set(f'''훈련 중... 남은 시간 {mm}분 {ss}초''')
            action_btn.configure(text = '훈련 중...', state = 'disabled')
            win.after(1000, refresh)
            return None
        if None >= TRAIN_MAX_PER_DAY:
            status_var.set(f'''오늘의 훈련 횟수를 다 썼어요 ({today_n}/{TRAIN_MAX_PER_DAY}). 내일 다시 와주세요!''')
            action_btn.configure(text = '오늘은 완료', state = 'disabled')
            return None
        None.set(f'''오늘 {today_n}/{TRAIN_MAX_PER_DAY}회 사용''')
        action_btn.configure(text = '▶ 훈련 시작하기 (1시간)', state = 'normal', command = start_session)

    claim_lock = {
        'busy': False }

    def start_session():
        '''train_session_start'''
        self.state['train_session_start'] = None()
        self.save_state()
        None()


    def claim():
        '''busy'''
        if claim_lock['busy']:
            return None
        claim_lock['busy'] = None
    
        try:
            action_btn.configure(state = 'disabled')
            start = self.state.get('train_session_start', 0)
            if bool(start):
                bool(start)
            session_done = None() - start >= TRAIN_SESSION_SECONDS
            if session_done or self._train_today_count() >= TRAIN_MAX_PER_DAY:
                claim_lock['busy'] = False
                None()
                return None
            self.state['train_atk_bonus_pct'] = time.time.train_bonus_pct() + TRAIN_ATK_BONUS_PER_SESSION
            self.state['train_session_start'] = 0
            self._train_bump_today()
            self.save_state()
            claim_lock['busy'] = False
            None('PikaPet', '훈련 완료! 공격력이 영구히 1% 올랐어요.')
            None()
            return None
        except Exception:
            continue


    None(body, textvariable = bonus_var, font = ('맑은 고딕', 10, 'bold'), fg = '#1a6b1a').pack(pady = (4, 2))
    None(body, textvariable = status_var, font = ('맑은 고딕', 9), fg = '#333', wraplength = 300).pack(pady = (2, 4))
    None()
    None(bottom, text = '닫기', command = win.destroy).pack()
    self._add_opacity_control(win)
