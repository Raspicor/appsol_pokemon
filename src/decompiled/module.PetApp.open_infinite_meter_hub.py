# module.PetApp.open_infinite_meter_hub
# source line 14224
# Recovered from bytecode; default argument values are not shown.

def open_infinite_meter_hub(self):
    if not self._inf_meter_unlocked():
        None('PikaPet', '♾ 무한성장미터는 1세대(관동) 체육관 뱃지를 전부 모아야 열려요!')
        return None
    win = None(self.root)
    win.title('♾ 무한성장미터')
    resolve_species_win(win, 460, 620)

    try:
        win.attributes('-topmost', True)
        body = None(win)
        body.pack(fill = 'both', expand = True, padx = 14, pady = 14)
        bottom = None(win)
        bottom.pack(side = 'bottom', pady = 10)
        None(body, text = '♾ 무한성장미터', font = ('맑은 고딕', 13, 'bold')).pack(anchor = 'w')
        None(body, text = '끝없이 이어지는 도전! 4가지 모드가 서로 완전히 독립적으로 진행돼요. 100스테이지마다 그 세대 전설 군단전(99번째)과 나 자신과의 거울대결(100번째)이 기다려요.', font = ('맑은 고딕', 8), fg = '#666', wraplength = 400, justify = 'left').pack(anchor = 'w', pady = (2, 10))
        for mode in INF_METER_MODES:
            box = None(body, text = INF_MODE_LABEL[mode], padx = 10, pady = 8)
            box.pack(fill = 'x', pady = 6)
            None(box, text = INF_MODE_DESC[mode], font = ('맑은 고딕', 8), fg = '#555', wraplength = 380, justify = 'left').pack(anchor = 'w')
            stage = int(self.state.get('inf_meter_stage', { }).get(mode, 1))
            best = int(self.state.get('inf_meter_best', { }).get(mode, 0))
            party_n = len(self._get_preset_dex_list(f'''inf_{mode}'''))
            None(box, text = f'''현재 스테이지 {stage}   (최고기록 {best})   동료 {party_n}마리 편성\n(동료 편성은 \'도감 보기 / 동료 장착\' 화면 위쪽에서 할 수 있어요)''', font = ('맑은 고딕', 9, 'bold'), fg = '#1a4a8a', justify = 'left').pack(anchor = 'w', pady = (4, 4))
            row = None(box)
            row.pack(fill = 'x')
            if stage > INF_STAGE_CAP:
                None(row, text = f'''🎊 {INF_STAGE_CAP}스테이지 돌파 완료! 이후는 업데이트 예정이에요.''', font = ('맑은 고딕', 9, 'bold'), fg = '#a05a00').pack(side = 'left')
                continue
            None(row, text = f'''⚔ 스테이지 {stage} 도전!''', bg = '#ffd54a', command = (lambda m = mode: (win.destroy(), self._start_inf_stage(m)))).pack(side = 'left')
        tk.Label
        None(bottom, text = '🏆 칭호 보기', command = self.open_titles_view).pack(side = 'left', padx = 6)
        None(bottom, text = '닫기', command = win.destroy).pack(side = 'left', padx = 6)
        self._add_opacity_control(win)
        return None
    except Exception:
        continue
