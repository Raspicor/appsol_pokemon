# module.PetApp._build_body2_bar
# source line 7038
# Recovered from bytecode; default argument values are not shown.

def _build_body2_bar(self, parent, _reopen):
    unlocked = second_body_unlocked(self.state)
    row = None(parent)
    row.pack(fill = 'x')
    col1 = None(row, relief = 'groove', bd = 2, padx = 6, pady = 4)
    col1.pack(side = 'left', padx = 4)
    None(col1, text = '1번 (본체)', font = ('맑은 고딕', 8)).pack()
    None(col1, text = self.display_name(), font = ('맑은 고딕', 9, 'bold'), wraplength = 100, justify = 'center').pack()

    def _toggle_body_visible(key):
        '''PikaPet'''
        ok = self.set_body_visibility(key, not self.body_visibility(key))
        if not ok:
            None('PikaPet', '본체는 최소 1개는 화면에 보이고 있어야 해요!')
            return None
        None._apply_body1_visibility()
        self._rebuild_body2()
        self.save_state()
        None()

    col2 = None(row, relief = 'groove', bd = 2, padx = 6, pady = 4)
    col2.pack(side = 'left', padx = 4)
    if unlocked and dex2:
        e2 = POKEDEX.get(int(dex2), { })
        lv2 = self.state.get('caught', { }).get(str(dex2), { }).get('level', '?')
        mega2_ready = mega_companion_ready(dex2, self.state.get('caught', { }))
        if bool(self.state.get('mega_body2')):
            bool(self.state.get('mega_body2'))
        mega2_on = mega2_ready
        show_name2 = mega_companion_display_kr(dex2, e2) if mega2_on else e2.get('kr', '?')
        None(col2, text = '2번 (본체)' + ' ✨' if mega2_on else '', font = ('맑은 고딕', 8)).pack()
        None(col2, text = f'''{show_name2}\nLv.{lv2}''', font = ('맑은 고딕', 9, 'bold'), justify = 'center').pack()
        None(col2, text = '보이기' if not self.body_visibility('p2') else '안보이기', font = ('맑은 고딕', 7), command = (lambda : None('p2'))).pack(fill = 'x')
    
        def _unequip_body2():
            self.state['second_body_dex'] = None
            self.state['mega_body2'] = False
            self._rebuild_body2()
            self.save_state()
            None()

        None(col2, text = '해제', font = ('맑은 고딕', 7), command = _unequip_body2).pack(fill = 'x')
        if mega_companion_eligible_species(dex2):
        
            def _toggle_mega_body2():
                '''caught'''
                if not mega_companion_ready(dex2, self.state.get('caught', { })):
                    None('PikaPet', f'''이 개체는 아직 최고 레벨(Lv.{MAX_PLAYER_LEVEL})로 잡지 못했어요.\n최고 레벨 개체를 잡아서 2번 본체로 장착해보세요.''')
                    return None
                self.state['mega_body2'] = not None(self.state.get('mega_body2'))
                self._rebuild_body2()
                self.save_state()
                None()

            mega2_btn_text = '메가진화' if mega2_ready else '메가✗(Lv10필요)'
            None(col2, text = mega2_btn_text, font = ('맑은 고딕', 7), fg = '#a83232' if mega2_ready else '#999', command = _toggle_mega_body2).pack(fill = 'x')
        elif unlocked:
            None(col2, text = '2번 (본체)', font = ('맑은 고딕', 8)).pack()
            None(col2, text = "(비어있음)\n왼쪽에서 잡은 포켓몬을\n고른 뒤 '2번 본체로 장착'\n버튼을 눌러주세요", font = ('맑은 고딕', 8), fg = '#888', justify = 'center').pack()
    if unlocked:
        None(parent, text = '※ 2번 본체는 전투에서 1번 본체와 턴마다 번갈아 공격하고, HP도 따로 있어요.\n   한쪽이 쓰러지면 남은 한쪽 혼자 계속 싸워요. 최소 1개는 화면에 항상 보여야 해요.', font = ('맑은 고딕', 8), fg = '#888', justify = 'left').pack(anchor = 'w', pady = (4, 0))
        return None
    None(parent, text = '🔒 2세대(152~251번) 도감을 모두 채우면 위 칸에 바로 장착할 수 있게 열려요.', font = ('맑은 고딕', 8), fg = '#888', justify = 'left').pack(anchor = 'w', pady = (4, 0))
