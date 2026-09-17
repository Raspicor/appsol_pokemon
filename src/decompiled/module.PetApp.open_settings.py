# module.PetApp.open_settings
# source line 18711
# Recovered from bytecode; default argument values are not shown.

def open_settings(self):
    win = None(self.root)
    win.title('설정')
    resolve_species_win(win, 560, 470)
    bottom = None(win)
    bottom.pack(side = 'bottom', pady = 8)
    body = None(win)
    body.pack(side = 'top', fill = 'both', expand = True, padx = 10)
    cols = None(body)
    cols.pack(fill = 'both', expand = True)
    left_col = None(cols)
    left_col.pack(side = 'left', fill = 'both', expand = True, padx = (0, 8))
    sep = None(cols, width = 1, bg = '#ccc')
    sep.pack(side = 'left', fill = 'y')
    right_col = None(cols)
    right_col.pack(side = 'left', fill = 'both', expand = True, padx = (8, 0))
    None(left_col, text = '포켓몬 애칭 (최대 8자, 비워두면 원래 이름 사용)', font = ('맑은 고딕', 9, 'bold'), wraplength = 250, justify = 'left').pack(pady = (14, 2), anchor = 'w')
    nick_row = None(left_col)
    nick_row.pack(fill = 'x')
    nick_var = None(value = self.state.get('nickname', ''))

    def _limit_nick(*_a):
        v = nick_var.get()
        if len(v) > 8:
            nick_var.set(v[<TYPE: 58>
    ])
            return None

    nick_var.trace_add('write', _limit_nick)
    nick_entry = None(nick_row, textvariable = nick_var, width = 14)
    nick_entry.pack(side = 'left', padx = (0, 6))

    def _save_nickname(*_a):
        val = nick_var.get().strip()[<TYPE: 58>
    ]
        nick_var.set(val)
        self.state['nickname'] = val
        self.save_state()

    None(nick_row, text = '저장', command = _save_nickname).pack(side = 'left')
    nick_entry.bind('<Return>', _save_nickname)
    None(left_col, text = '움직이는 속도').pack(pady = (14, 2), anchor = 'w')
    var = None(value = self.state.get('speed_mult', 1))

    def _on_change(v):
        '''speed_mult'''
        self.state['speed_mult'] = float(v)
        self.save_state()

    None(left_col, from_ = 0.5, to = 2, resolution = 0.1, orient = 'horizontal', variable = var, command = _on_change, length = 220).pack(anchor = 'w')
    None(left_col, text = '야생 포켓몬 조우 알림 방식', font = ('맑은 고딕', 9, 'bold')).pack(pady = (14, 2), anchor = 'w')
    notify_var = None(value = self.state.get('encounter_notify_mode', 'blink'))

    def _on_notify(*_a):
        '''encounter_notify_mode'''
        self.state['encounter_notify_mode'] = notify_var.get()
        self.save_state()

    None(left_col, text = '즉시 창 띄우기', variable = notify_var, value = 'popup', command = _on_notify).pack(anchor = 'w')
    None(left_col, text = '3초 작은 팝업으로 알려주기 (Fight 버튼)', variable = notify_var, value = 'toast', command = _on_notify).pack(anchor = 'w')
    None(left_col, text = '조용히 트레이 아이콘 깜빡이기 (추천)', variable = notify_var, value = 'blink', command = _on_notify).pack(anchor = 'w')
    None(left_col, text = '야생 3초 팝업 글자색', font = ('맑은 고딕', 8)).pack(pady = (6, 0), anchor = 'w')
    wild_toast_color_var = None(value = self.state.get('wild_toast_color_mode', 'black'))

    def _on_wild_toast_color(*_a):
        '''wild_toast_color_mode'''
        self.state['wild_toast_color_mode'] = wild_toast_color_var.get()
        self.save_state()

    toast_color_row1 = None(left_col)
    toast_color_row1.pack(anchor = 'w')
    None(toast_color_row1, text = '흑색 (기본)', variable = wild_toast_color_var, value = 'black', font = ('맑은 고딕', 8), command = _on_wild_toast_color).pack(side = 'left')
    None(toast_color_row1, text = '컬러(예전 색)', variable = wild_toast_color_var, value = 'color', font = ('맑은 고딕', 8), command = _on_wild_toast_color).pack(side = 'left')
    None(left_col, text = '모니터 설정 (듀얼모니터 쓰시는 분만)', font = ('맑은 고딕', 9, 'bold'), wraplength = 250, justify = 'left').pack(pady = (14, 2), anchor = 'w')
    if self.state.get('secondary_monitor_mode'):
        _monitor_init = 'secondary'
    elif self.state.get('single_monitor_mode'):
        _monitor_init = 'single'
    else:
        _monitor_init = 'multi'
    monitor_var = None(value = _monitor_init)

    def _on_monitor(*_a):
        '''single'''
        v = monitor_var.get()
        self.set_single_monitor_mode(v == 'single')
        self.set_secondary_monitor_mode(v == 'secondary')

    None(left_col, text = '기존 설정 (모든 모니터를 다 사용)', variable = monitor_var, value = 'multi', command = _on_monitor, wraplength = 250, justify = 'left').pack(anchor = 'w')
    None(left_col, text = '주 모니터만 사용 (야생조우·알림·이동을 주 모니터 안에만)', variable = monitor_var, value = 'single', command = _on_monitor, wraplength = 250, justify = 'left').pack(anchor = 'w')
    None(left_col, text = '보조 모니터만 사용 (야생조우·알림·이동을 보조 모니터 안에만)', variable = monitor_var, value = 'secondary', command = _on_monitor, wraplength = 250, justify = 'left').pack(anchor = 'w')
    None(right_col, text = '팝업 등장 위치 (야생조우·로켓단·수련의방 등 공통)', font = ('맑은 고딕', 9, 'bold'), wraplength = 250, justify = 'left').pack(pady = (14, 2), anchor = 'w')
    rocket_loc_var = None(value = self.state.get('rocket_ambush_location', 'any'))

    def _on_rocket_loc(*_a):
        '''rocket_ambush_location'''
        self.state['rocket_ambush_location'] = rocket_loc_var.get()
        self.save_state()

    None(right_col, text = '아무 데나 (지금 이동범위 그대로, 기본)', variable = rocket_loc_var, value = 'any', command = _on_rocket_loc, wraplength = 250, justify = 'left').pack(anchor = 'w')
    None(right_col, text = '주 모니터에만 등장', variable = rocket_loc_var, value = 'main', command = _on_rocket_loc).pack(anchor = 'w')
    None(right_col, text = '보조 모니터에만 등장', variable = rocket_loc_var, value = 'secondary', command = _on_rocket_loc).pack(anchor = 'w')
    None(right_col, text = '전체 팝업 안 뜨기 (야생조우·로켓단·수련의방 알림창 다 끄기)', variable = rocket_loc_var, value = 'off', command = _on_rocket_loc, wraplength = 250, justify = 'left').pack(anchor = 'w')
    None(right_col, text = '로켓단 팝업 색상', font = ('맑은 고딕', 8)).pack(pady = (6, 0), anchor = 'w')
    rocket_color_var = None(value = self.state.get('rocket_popup_color_mode', 'black'))

    def _on_rocket_color(*_a):
        '''rocket_popup_color_mode'''
        self.state['rocket_popup_color_mode'] = rocket_color_var.get()
        self.save_state()

    rocket_color_row = None(right_col)
    rocket_color_row.pack(anchor = 'w')
    None(rocket_color_row, text = '흑색 (기본)', variable = rocket_color_var, value = 'black', font = ('맑은 고딕', 8), command = _on_rocket_color).pack(side = 'left')
    None(rocket_color_row, text = '컬러(예전 색)', variable = rocket_color_var, value = 'color', font = ('맑은 고딕', 8), command = _on_rocket_color).pack(side = 'left')
    None(right_col, text = '팝업 유지 시간 (야생조우·로켓단·수련의방 등 공통)', font = ('맑은 고딕', 9, 'bold'), wraplength = 250, justify = 'left').pack(pady = (14, 2), anchor = 'w')
    toast_dur_var = None(value = int(self.state.get('toast_duration_sec', 5)))

    def _on_toast_dur(*_a):
        '''toast_duration_sec'''
        self.state['toast_duration_sec'] = toast_dur_var.get()
        self.save_state()

    for label, secs in (('1초', 1), ('3초', 3), ('5초 (기본)', 5), ('7초', 7), ('10초', 10), ('안 끔 (직접 눌러야만 사라짐)', 0)):
        None(right_col, text = label, variable = toast_dur_var, value = secs, command = _on_toast_dur).pack(anchor = 'w')
    (('1초', 1), ('3초', 3), ('5초 (기본)', 5), ('7초', 7), ('10초', 10), ('안 끔 (직접 눌러야만 사라짐)', 0))
    None(right_col, text = '바탕화면 포켓몬이 깜짝 숨었다가 나오는 시간', font = ('맑은 고딕', 9, 'bold'), wraplength = 250, justify = 'left').pack(pady = (14, 2), anchor = 'w')
    hide_var = None(value = self.state.get('pet_hide_seconds', 8))

    def _on_hide(*_a):
        '''pet_hide_seconds'''
        self.state['pet_hide_seconds'] = hide_var.get()
        self.save_state()

    for label, secs in (('3초', 3), ('8초 (기본)', 8), ('15초', 15), ('30초', 30), ('사라지지 않음 (이 행동 자체를 안 함)', 0)):
        None(right_col, text = label, variable = hide_var, value = secs, command = _on_hide).pack(anchor = 'w')
    (('3초', 3), ('8초 (기본)', 8), ('15초', 15), ('30초', 30), ('사라지지 않음 (이 행동 자체를 안 함)', 0))
    None(right_col, text = '※ 먹이 · 재주 · 도감 · 몬스터볼 같은 기능은\n마우스 우클릭 메뉴에서 할 수 있어요.', font = ('맑은 고딕', 8), fg = '#888', justify = 'left', wraplength = 250).pack(pady = 10, anchor = 'w')
    None(right_col, text = '처음부터 다시 키우기', fg = '#b00000', command = self.reset_pet).pack(pady = (4, 4), anchor = 'w')
    None(body, text = '제작자 Instagram @do_bro.2 · © 2026 do_bro.2. All rights reserved.', font = ('맑은 고딕', 8), fg = '#999', justify = 'center').pack(side = 'bottom', pady = (6, 0))
    None(bottom, text = '닫기', command = win.destroy).pack()
    self._add_opacity_control(win)
    win.resizable(True, True)

    try:
        win.update_idletasks()
        req_w = win.winfo_reqwidth() + 10
        req_h = win.winfo_reqheight() + 10
        sh = win.winfo_screenheight()
        sw = win.winfo_screenwidth()
        final_w = min(max(req_w, 560), sw - 60)
        final_h = min(max(req_h, 470), sh - 100)
        win.geometry(f'''{final_w}x{final_h}''')
        return None
    except Exception:
        tk.Label
        return None
