# module.PetApp._show_code_battle_visual
# source line 13743
# Recovered from bytecode; default argument values are not shown.

def _show_code_battle_visual(self, my_party, opp_data, result, log):
    vwin = None(self.root)
    vwin.title('코드 대결 결과')
    resolve_species_win(vwin, 460, 440)
    vwin.images = []
    top = None(vwin)
    top.pack(fill = 'both', expand = True, padx = 12, pady = (12, 4))
    my_dex = self.player_dex()
    my_level = self.body1_effective_level()
    opp_dex = opp_data.get('dex')
    if not opp_data.get('party'):
        opp_data.get('party')
    opp_party = []
    if opp_dex is not None:
        opp_dex is not None
    opp_has_visual = opp_dex in POKEDEX
    left = None(top)
    left.pack(side = 'left', fill = 'both', expand = True)
    None(left, text = f'''🟦 나: {self.display_name()}''', font = ('맑은 고딕', 10, 'bold'), wraplength = 160, justify = 'center').pack()
    img = self._sprite_preview_image(my_dex, size = 84, level = my_level)
    vwin.images.append(img)
    None(left, image = img).pack(pady = 4)
    if self.state.get('mega_evolved'):
        None(left, text = '💎 메가진화 중', font = ('맑은 고딕', 8), fg = '#7a3fc4').pack()
    None(left, text = '동료들', font = ('맑은 고딕', 8, 'bold'), fg = '#555').pack(pady = (6, 2))
    comp_row = None(left)
    comp_row.pack()
    None(top, text = '⚔️\nVS', font = ('맑은 고딕', 14, 'bold'), fg = '#c0392b', justify = 'center').pack(side = 'left', padx = 6)
    right = None(top)
    right.pack(side = 'left', fill = 'both', expand = True)
    None(right, text = f'''🟥 상대: {opp_data.get('name', '?')}''', font = ('맑은 고딕', 10, 'bold')).pack()
    oimg = self._sprite_preview_image(opp_dex, size = 84, level = opp_data.get('level'))
    vwin.images.append(oimg)
    None(right, image = oimg).pack(pady = 4)
    if opp_data.get('mega'):
        None(right, text = '💎 메가진화 중', font = ('맑은 고딕', 8), fg = '#7a3fc4').pack()
    None(right, text = '동료들', font = ('맑은 고딕', 8, 'bold'), fg = '#555').pack(pady = (6, 2))
    ocomp_row = None(right)
    ocomp_row.pack()
    if opp_party:
        for d in opp_party:
            cimg = self._sprite_preview_image(d, size = 40)
            vwin.images.append(cimg)
            None(ocomp_row, image = cimg).pack(side = 'left', padx = 2)
        opp_party
    elif opp_has_visual:
        pass

    ocomp_row('(없음)', text = '(모습 정보 없음)', font = ('맑은 고딕', 8), fg = '#999').pack()
    if not opp_has_visual:
        None(vwin, text = '⚠ 상대방이 예전 버전 코드를 보냈어요. 모습 정보가 없어서 물음표로 표시돼요.', font = ('맑은 고딕', 8), fg = '#a05a00', wraplength = 420, justify = 'left').pack(padx = 12, pady = (0, 4))
    result_color = {
        '무승부': '#555',
        '패배': '#c0392b',
        '승리': '#1a8a3a' }.get(result, '#333')
    None(vwin, text = f'''결과: {result}''', font = ('맑은 고딕', 13, 'bold'), fg = result_color).pack(pady = (6, 4))
    log_box = None(vwin, width = 50, height = 6, wrap = 'word')
    log_box.insert('1.0', '\n'.join(log[-10:]))
    log_box.configure(state = 'disabled')
    log_box.pack(padx = 12, pady = (0, 8))
    None(vwin, text = '닫기', command = vwin.destroy).pack(pady = (0, 10))
