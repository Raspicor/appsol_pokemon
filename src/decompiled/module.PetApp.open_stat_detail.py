# module.PetApp.open_stat_detail
# source line 12544
# Recovered from bytecode; default argument values are not shown.

def open_stat_detail(self):
    win = None(self.root)
    win.title('내 스탯 자세히 보기')
    resolve_species_win(win, 360, 620)
    bottom = None(win)
    bottom.pack(side = 'bottom', pady = 10)
    body_outer = None(win)
    body_outer.pack(side = 'top', fill = 'both', expand = True, padx = 14, pady = (14, 0))
    body_canvas = None(body_outer, highlightthickness = 0)
    body_vsb = None(body_outer, orient = 'vertical', command = body_canvas.yview)
    body = None(body_canvas)
    _body_win_id = body_canvas.create_window((0, 0), window = body, anchor = 'nw')
    body.bind('<Configure>', (lambda e: body_canvas.configure(scrollregion = body_canvas.bbox('all'))))
    body_canvas.bind('<Configure>', (lambda e: body_canvas.itemconfig(_body_win_id, width = e.width)))
    body_canvas.configure(yscrollcommand = body_vsb.set)
    body_canvas.pack(side = 'left', fill = 'both', expand = True)
    body_vsb.pack(side = 'right', fill = 'y')

    def _stat_wheel(event):
        '''num'''
        delta = -1 if getattr(event, 'num', 0) == 5 or event.delta < 0 else 1
    
        try:
            if body_canvas.winfo_exists():
            
                try:
                    body_canvas.yview_scroll(-delta, 'units')
                    return None
                    return None
                except Exception:
                    return None



    win.bind('<MouseWheel>', _stat_wheel)
    win.bind('<Button-4>', _stat_wheel)
    win.bind('<Button-5>', _stat_wheel)
    conf = self.stage_conf()
    entry = self.player_pokedex_entry()
    cap = companion_slot_count(self.state)
    party = list(self.state.get('party', []))[:cap]
    atk_pct = ()
    def_pct = companion_synergy_bonus(party, self.state.get('caught', { }), self.state.get('mega_party', []))
    self.state.get('custom_body_dex') = self.player_battle_stats(atk_pct = atk_pct, def_pct = def_pct, crit_bonus = crit_pct)
    disp_level = self.body1_effective_level()
    None(body, text = f'''{self.display_name()} (Lv.{disp_level}{'  ·  메가진화 중' if not self.state.get('mega_evolved') and custom_dex_now else ''})''', font = ('맑은 고딕', 12, 'bold'), wraplength = 320, justify = 'left').pack(anchor = 'w', pady = (0, 4))
    None(body, text = f'''HP {bs['hp']}   공격 {bs['atk']}   방어 {bs['def']}   크리티컬 {bs['crit']:.0f}%''', font = ('맑은 고딕', 11, 'bold'), fg = '#1a4a8a').pack(anchor = 'w', pady = (0, 2))
    None(body, text = '(위 수치는 동료 시너지·수련·미니게임·체육관 뱃지·메가진화가 전부 반영된 최종 값이에요)', font = ('맑은 고딕', 7), fg = '#999').pack(anchor = 'w', pady = (0, 6))
    if custom_dex_now:
        None(body, text = '※ 본체를 교체한 상태예요. 이제 원래 스타터 레벨을 빌려쓰거나\n상한선을 씌우지 않고, 이 종 자신의 레벨/능력치를 그대로 써요.', font = ('맑은 고딕', 7), fg = '#a83a8a', justify = 'left', wraplength = 320).pack(anchor = 'w', pady = (0, 4))
        if self._is_raised(custom_dex_now):
            lineage_txt = self._raised_lineage_text(custom_dex_now)
            None(body, text = f'''🌟 직접 키운 개체예요! (HP/공격/방어 +{int(round((RAISED_STAT_BONUS_MULT - 1) * 100))}% 보너스 적용 중)\n성장 계보: {lineage_txt}''', font = ('맑은 고딕', 7, 'bold'), fg = '#c07a1a', justify = 'left', wraplength = 320).pack(anchor = 'w', pady = (0, 4))
    None(body, text = f'''⚔ 총 추가 공격력: +{self.total_extra_atk_pct():.1f}%  (수련 +{self.train_bonus_pct():.1f}%  ·  미니게임 +{self.minigame_bonus_pct():.1f}%)''', font = ('맑은 고딕', 8, 'bold'), fg = '#1a6b1a', wraplength = 320, justify = 'left').pack(anchor = 'w', pady = (0, 2))
    None(body, text = f'''🏅 체육관 뱃지 최종공격력: +{gym_badge_atk_bonus_pct(self.state):.1f}%  ({len(gym_badges_held(self.state))}/{len(GYM_LEADERS)}개 보유, 위 총 추가 공격력 위에 별도로 곱해져요)''', font = ('맑은 고딕', 8, 'bold'), fg = '#a8681a', wraplength = 320, justify = 'left').pack(anchor = 'w', pady = (0, 2))
    title_atk_pct_now = title_atk_bonus_pct(self.state)
    n_titles_atk = (lambda .0: for t in .0:
    if not isinstance(t.get('id') if isinstance(t, dict) else t, str):
    continueif not t.get('id') if isinstance(t, dict) else t.startswith('inf_stage_') and t.get('id') if isinstance(t, dict) else t.endswith('_master'):
    continue1.0)(self.state.get('titles_earned', [])())
    None(body, text = f'''🏆 칭호 최종공격력: +{title_atk_pct_now:.1f}%  ({n_titles_atk}개 칭호 보유, 체육관 뱃지와 똑같이 위 총 추가 공격력 위에 별도로 곱해져요)''', font = ('맑은 고딕', 8, 'bold'), fg = '#7a3fa8', wraplength = 320, justify = 'left').pack(anchor = 'w', pady = (0, 2))
    _t_def_disp = title_def_bonus_pct(self.state)
    _t_hp_pct_disp = title_hp_pct_bonus(self.state)
    _t_hp_flat_disp = title_hp_flat_bonus(self.state)
    _t_crit_disp = title_crit_bonus_pct(self.state)
    _title_extra_bits = []
    if _t_def_disp:
        _title_extra_bits.append(f'''방어 +{_t_def_disp:.1f}%''')
    if _t_hp_pct_disp:
        _title_extra_bits.append(f'''HP +{_t_hp_pct_disp:.1f}%''')
    if _t_hp_flat_disp:
        _title_extra_bits.append(f'''HP +{_t_hp_flat_disp:.0f}(고정)''')
    if _t_crit_disp:
        _title_extra_bits.append(f'''크리티컬 +{_t_crit_disp:.1f}%p''')
    if _title_extra_bits:
        None(body, text = '🏆 칭호 추가 보너스: ' + '  '.join(_title_extra_bits) + '  (위 최종 HP/방어/크리티컬 수치에 이미 반영돼 있어요)', font = ('맑은 고딕', 8, 'bold'), fg = '#7a3fa8', wraplength = 320, justify = 'left').pack(anchor = 'w', pady = (0, 2))
    title_all_mult_now = title_stat_mult(self.state)
    if title_all_mult_now != 1:
        None(body, text = f'''🌟 칭호 총 스탯 배율: ×{title_all_mult_now:.2f}  (400/800스테이지 칭호 보너스, HP·공격·방어 전부에 마지막으로 한 번 더 곱해져요)''', font = ('맑은 고딕', 8, 'bold'), fg = '#c0392b', wraplength = 320, justify = 'left').pack(anchor = 'w', pady = (0, 2))
    calc_mega_mult = 1 if custom_dex_now else self.mega_mult()
    None(body, text = mega_mult_txt + '  (본체 교체 중엔 적용 안 됨)' if custom_dex_now else '', font = ('맑은 고딕', 8), fg = '#888', wraplength = 320, justify = 'left').pack(anchor = 'w', pady = (0, 6))
    b2 = self.body2_battle_stats(atk_pct = atk_pct, def_pct = def_pct, crit_bonus = crit_pct)
    sep2 = None(body, height = 1, bg = '#ddd')
    sep2.pack(fill = 'x', pady = (4, 8))
    calc_frame = None(body, text = '📐 최종공격력은 이렇게 계산돼요', padx = 8, pady = 6)
    calc_frame.pack(fill = 'x', pady = (0, 10))
    lvl = disp_level
    step1_bs = battle_stats(entry, lvl, atk_pct = 0, extra_atk_pct = 0, perm_atk_pct = 0, own_starter_stage = None if custom_dex_now else self.starter_remaining_stages(), mega_mult = calc_mega_mult, mega_atk_mult = calc_mega_atk_mult, mega_def_mult = calc_mega_def_mult, raised_bonus = self._is_raised(custom_dex_now) if custom_dex_now else False)
    step1 = step1_bs['atk']
    train_pct = self.train_bonus_pct()
    mg_pct = self.minigame_bonus_pct()
    comp_pct = atk_pct
    extra_pct = comp_pct + train_pct + mg_pct
    step2 = int(round(step1 * (1 + extra_pct / 100)))
    badge_pct = gym_badge_atk_bonus_pct(self.state)
    title_pct = title_atk_bonus_pct(self.state)
    perm_pct = badge_pct + title_pct
    step3 = int(round(step2 * (1 + perm_pct / 100))) if perm_pct else step2
    all_mult = title_stat_mult(self.state)
    step4 = int(round(step3 * all_mult)) if all_mult != 1 else step3
    None(calc_frame, text = f'''② 동료 시너지 +{comp_pct:.1f}%  +  수련 +{train_pct:.1f}%  +  미니게임 +{mg_pct:.1f}%  (합 +{extra_pct:.1f}%)\n    {step1} × (1 + {extra_pct:.1f}%) = {step2}''', font = ('맑은 고딕', 8), justify = 'left', anchor = 'w', wraplength = 320).pack(anchor = 'w', fill = 'x', pady = (4, 0))
    None(calc_frame, text = f'''③ 체육관 뱃지 +{badge_pct:.1f}% ({len(gym_badges_held(self.state))}개)  +  칭호 +{title_pct:.1f}% ({n_titles_atk}개)  (합 +{perm_pct:.1f}%)\n    {step2} × (1 + {perm_pct:.1f}%) = {step3}''' + '  ← 최종공격력' if all_mult == 1 else '', font = ('맑은 고딕', 8, 'bold'), fg = '#1a4a8a', justify = 'left', anchor = 'w', wraplength = 320).pack(anchor = 'w', fill = 'x', pady = (4, 0))
    if all_mult != 1:
        None(calc_frame, text = f'''④ 칭호 총 스탯 배율 ×{all_mult:.2f} (400/800스테이지 칭호)\n    {step3} × {all_mult:.2f} = {step4}  ← 최종공격력''', font = ('맑은 고딕', 8, 'bold'), fg = '#c0392b', justify = 'left', anchor = 'w', wraplength = 320).pack(anchor = 'w', fill = 'x', pady = (4, 0))
    None(calc_frame, text = '※ 뱃지·칭호 보너스는 ②까지 다 반영된 값 위에 곱해져서, %가 조금만 올라도\n실제 공격력 증가폭은 그보다 작게 보일 수 있어요 (정상 동작이에요).', font = ('맑은 고딕', 7), fg = '#999', justify = 'left', wraplength = 320).pack(anchor = 'w', pady = (4, 0))
    None(body, text = '동료별 능력치 기여도 (레벨이 높을수록 보너스가 세져요)', font = ('맑은 고딕', 10, 'bold')).pack(anchor = 'w', pady = (2, 4))
    rows = companion_synergy_breakdown(party, self.state.get('caught', { }), self.state.get('mega_party', []))
    None(bottom, text = '닫기', command = win.destroy).pack()
    self._add_opacity_control(win)
