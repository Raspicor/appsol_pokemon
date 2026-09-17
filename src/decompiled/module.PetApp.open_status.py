# module.PetApp.open_status
# source line 18350
# Recovered from bytecode; default argument values are not shown.

def open_status(self):
    win = None(self.root)
    win.title('상태 보기')
    resolve_species_win(win, 370, 560)

    try:
        win.geometry('370x560')
        bottom = None(win)
        bottom.pack(side = 'bottom', pady = 10)
        scroll_hint = None(win, bg = '#eef3ff')
        scroll_hint.pack(side = 'top', fill = 'x')
        None(scroll_hint, text = '🖱 마우스 휠로 내려보면 더 많은 정보가 있어요 ⬇', font = ('맑은 고딕', 8, 'bold'), fg = '#3a5a9a', bg = '#eef3ff').pack(pady = 3)
        outer_canvas = None(win, highlightthickness = 0)
        vscroll = None(win, orient = 'vertical', command = outer_canvas.yview, width = 18)
        outer_canvas.configure(yscrollcommand = vscroll.set)
        outer_canvas.pack(side = 'left', fill = 'both', expand = True)
        vscroll.pack(side = 'right', fill = 'y')
        body = None(outer_canvas)
        body_win_id = outer_canvas.create_window((0, 0), window = body, anchor = 'nw')
    
        def _on_body_configure(evt = None):
            '''all'''
        
            try:
                outer_canvas.configure(scrollregion = outer_canvas.bbox('all'))
                return None
            except Exception:
                return None


        body.bind('<Configure>', _on_body_configure)
    
        def _on_status_canvas_configure(evt):
        
            try:
                outer_canvas.itemconfig(body_win_id, width = evt.width)
                return None
            except Exception:
                return None


        outer_canvas.bind('<Configure>', _on_status_canvas_configure)
    
        def _on_status_wheel(evt):
        
            try:
                if evt.delta > 0:
                
                    try:
                        pass
                    return None
                    except Exception:
                        return None



    
        def _bind_status_wheel(evt = None):
            '''<MouseWheel>'''
        
            try:
                outer_canvas.bind_all('<MouseWheel>', _on_status_wheel)
                return None
            except Exception:
                return None


    
        def _unbind_status_wheel(evt = None):
            '''<MouseWheel>'''
        
            try:
                outer_canvas.unbind_all('<MouseWheel>')
                return None
            except Exception:
                return None


        outer_canvas.bind('<Enter>', _bind_status_wheel)
        outer_canvas.bind('<Leave>', _unbind_status_wheel)
        outer_canvas.bind('<Destroy>', _unbind_status_wheel, add = '+')
        conf = self.stage_conf()
        starter_name = self.starter_stage_conf().get('kr', '스타터')
        None(body, text = f'''이름: {self.display_name()}''', font = ('맑은 고딕', 12, 'bold'), wraplength = 340, justify = 'left').pack(anchor = 'w', padx = 14, pady = (14, 2))
        None(body, text = f'''플레이어 레벨: {self.player_level()}  (동료 {companion_slot_count(self.state)}칸 사용 가능)''', font = ('맑은 고딕', 9), fg = '#1a4a8a').pack(anchor = 'w', padx = 14, pady = (0, 2))
        note = f'''※ 전체 레벨/최대 레벨은 항상 스타터 \'{starter_name}\' 기준(게임 진행도)이에요.'''
        if self.state.get('custom_body_dex'):
            note += '\n   (지금 화면엔 다른 포켓몬이 본체로 나와있지만, 레벨은 스타터 걸 그대로 써요)'
        None(body, text = note, font = ('맑은 고딕', 8), fg = '#888', justify = 'left', wraplength = 330).pack(anchor = 'w', padx = 14, pady = (0, 2))
        None(body, text = player_level_progress_text(self.state), font = ('맑은 고딕', 8), fg = '#555').pack(anchor = 'w', padx = 14, pady = (0, 8))
    
        def bar(label, value):
            '''x'''
            f = None(body)
            f.pack(fill = 'x', padx = 14, pady = 4)
            None(f, text = label, width = 10, anchor = 'w').pack(side = 'left')
            pb = None(f, length = 140, maximum = 100, value = max(0, min(100, value)))
            pb.pack(side = 'left', padx = 6)
            None(f, text = f'''{int(value)}%''').pack(side = 'left')

        None('포만감', self.state.get('hunger', 80))
        None('애정도', self.state.get('affection', 50))
        None('체중', self.state.get('weight', 50))
        roster_frame = None(body, text = '🆙🧬 레벨업/진화 현황', padx = 8, pady = 4)
        roster_frame.pack(fill = 'x', padx = 14, pady = (2, 8))
        for ln in self._status_roster_dday_lines():
            None(roster_frame, text = ln, font = ('맑은 고딕', 8), fg = '#333', anchor = 'w', justify = 'left', wraplength = 300).pack(anchor = 'w', pady = 1)
        self._status_roster_dday_lines()
        None(body, text = self.evolution_progress_text(), font = ('맑은 고딕', 9), fg = '#333').pack(pady = (10, 2))
        None(body, text = self.daily_quest_text(), font = ('맑은 고딕', 9), fg = '#333').pack(pady = (0, 4))
        None(body, text = f'''⚔ 총 추가 공격력: +{self.total_extra_atk_pct():.1f}%  (수련의 방 +{self.train_bonus_pct():.1f}%  ·  미니게임 +{self.minigame_bonus_pct():.1f}%)''', font = ('맑은 고딕', 9, 'bold'), fg = '#1a6b1a', justify = 'left', wraplength = 330).pack(pady = (0, 4))
        gym_held = sorted(gym_badges_held(self.state))
        gym_total = len(GYM_LEADERS)
        None(body, text = f'''🏅 체육관 뱃지: {len(gym_held)}/{gym_total}  (최종공격력 +{gym_badge_atk_bonus_pct(self.state):.1f}%, 위 총 추가 공격력 위에 별도로 곱해져요)''', font = ('맑은 고딕', 9, 'bold'), fg = '#a8681a', wraplength = 330, justify = 'left').pack(pady = (2, 2))
        if self.is_eevee_base():
            et = self.state.get('element_train', { })
            None(body, text = f'''불 훈련 {et.get('fire', 0)}회 · 물 훈련 {et.get('water', 0)}회 · 번개 훈련 {et.get('electric', 0)}회''', font = ('맑은 고딕', 9)).pack(pady = 6)
        evo_hint_frame = None(body, relief = 'groove', bd = 1)
        evo_hint_frame.pack(fill = 'x', padx = 14, pady = (0, 8))
        hint_txt = '✅ 진화 가능해요! 아래 버튼으로 진화/레벨 탭을 열어보세요.' if self.evolution_ready() else "진화 조건, 다음 진화 미리보기, 이브이 갈래 선택은 모두 '🧬 진화/레벨 탭'에서 볼 수 있어요."
        None(evo_hint_frame, text = hint_txt, font = ('맑은 고딕', 8, 'bold' if self.evolution_ready() else 'normal'), fg = '#a83a8a' if self.evolution_ready() else '#555', justify = 'left', wraplength = 310).pack(anchor = 'w', padx = 6, pady = (6, 2))
        None(evo_hint_frame, text = '🧬 진화/레벨 탭 열기', font = ('맑은 고딕', 8), command = (lambda : (win.destroy(), self.open_evolution_tab()))).pack(anchor = 'w', padx = 6, pady = (0, 6))
        caught = self.state.get('caught', { })
        dex_seen = self.state.get('dex', { })
        missed_n = len(self.state.get('missed', { }))
        None(body, text = '📖 세대별 도감 현황', font = ('맑은 고딕', 9, 'bold'), fg = '#333').pack(pady = (4, 2))
        for gen, start, end in gen_dex_ranges():
            total = end - start
            c_n = (lambda .0: for d in .0:
    if not str(d) in caught:
    continue1.0)(range(start, end)())
            s_n = (lambda .0: for d in .0:
    if not str(d) in dex_seen:
    continue1.0)(range(start, end)())
            None(body, text = f'''{gen}세대: {c_n}/{total} 잡음 · {s_n}/{total} 만남''', font = ('맑은 고딕', 9)).pack(pady = (0, 1))
        sum
        None(body, text = f'''⟲ {missed_n}마리 재도전 가능''', font = ('맑은 고딕', 8), fg = '#888').pack(pady = (2, 4))
        secs = int(self.state.get('active_seconds', 0))
        None(body, text = f'''함께한 시간: {secs // 3600}시간 {(secs % 3600) // 60}분''', font = ('맑은 고딕', 9)).pack(pady = (6, 4))
        None(bottom, text = '닫기', command = win.destroy).pack()
        self._add_opacity_control(win)
        return None
    except Exception:
        continue
