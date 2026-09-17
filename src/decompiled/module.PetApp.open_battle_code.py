# module.PetApp.open_battle_code
# source line 12770
# Recovered from bytecode; default argument values are not shown.

def open_battle_code(self):
    win = None(self.root)
    win.title('코드 대결')
    resolve_species_win(win, 380, 480)
    bottom = None(win)
    bottom.pack(side = 'bottom', pady = 10)
    body = None(win)
    body.pack(side = 'top', fill = 'both', expand = True, padx = 14, pady = (14, 0))
    None(body, text = '🔑 코드 대결 (오프라인)', font = ('맑은 고딕', 13, 'bold')).pack(pady = (0, 4))
    None(body, text = '실시간으로 연결되진 않지만, 서로 코드를 주고받으면\n상대 포켓몬 기록을 불러와서 내 게임에서 혼자 모의전투를 해볼 수 있어요.', font = ('맑은 고딕', 8), fg = '#666', justify = 'left', wraplength = 330).pack(pady = (0, 6))
    None(body, text = '🎒 코드 대결용 동료 편성', command = (lambda : self.open_preset_editor('code'))).pack(fill = 'x', pady = (0, 10))
    None(body, text = '① 내 코드 내보내기', font = ('맑은 고딕', 9, 'bold')).pack(anchor = 'w')
    code_entry = None(body, width = 40)
    code_entry.pack(pady = (4, 2), fill = 'x')

    def _export():
        payload = self._build_battle_code_payload()
        code = encode_battle_code(payload)
        code_entry.delete(0, 'end')
        if not code:
            code
        code_entry.insert(0, '')
        code_entry.select_range(0, 'end')
        code_entry.focus_set()

    None(body, text = '내 코드 만들기 (자동으로 선택돼요, Ctrl+C로 복사)', command = _export).pack(fill = 'x', pady = (0, 12))
    None(body, text = '② 상대 코드로 대결하기', font = ('맑은 고딕', 9, 'bold')).pack(anchor = 'w')
    opp_entry = None(body, width = 40)
    opp_entry.pack(pady = (4, 4), fill = 'x')
    None(body, text = '체육관 전투처럼 직접 필살기/공격/방어를 골라가며 싸워요.', font = ('맑은 고딕', 8), fg = '#666').pack(anchor = 'w', pady = (0, 4))

    def _fight():
        '''PikaPet'''
        data = decode_battle_code(opp_entry.get())
        if not data:
            None('PikaPet', '코드가 올바르지 않아요. 정확히 복사해서 붙여넣어 주세요.')
            return None
        None.destroy()
        self._open_code_battle_window(data)

    None(body, text = '이 코드로 대결하기! (직접 조작)', command = _fight).pack(fill = 'x')
    history = self.state.get('battle_code_log', [])
    if history:
        None(body, text = f'''최근 기록: {len(history)}건 (최신 5건)''', font = ('맑은 고딕', 8, 'bold'), fg = '#555').pack(anchor = 'w', pady = (10, 2))
        for h in history[-5:][::-1]:
            None(body, text = f'''{h.get('when', '?')}  vs {h.get('opponent', '?')}  →  {h.get('result', '?')}''', font = ('맑은 고딕', 8), fg = '#777').pack(anchor = 'w')
        history[-5:][::-1]
    None(bottom, text = '닫기', command = win.destroy).pack()
    self._add_opacity_control(win)
