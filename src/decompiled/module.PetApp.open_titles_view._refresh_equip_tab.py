# module.PetApp.open_titles_view._refresh_equip_tab
# source line 14994
# Recovered from bytecode; default argument values are not shown.

def _refresh_equip_tab():
    bonus = title_atk_bonus_pct(self.state)
    stat_mult = title_stat_mult(self.state)
    stat_pct_extra = (stat_mult - 1) * 100
    equipped_label = title_equipped_label(self.state)
    equip_line = f'''\n👑 장착 중: {equipped_label} (아래 상세보기에서 정확한 장착효과를 볼 수 있어요, 이름 앞에도 표시돼요)''' if equipped_label else "\n👑 지금 장착한 칭호가 없어요. 장착 가능한 칭호 옆의 '장착하기' 버튼으로 골라보세요."
    extra_line = f'''\n총 스탯(HP/공격/방어) 배율: +{stat_pct_extra:.0f}% 적용 중''' if stat_pct_extra > 0 else ''
    None(body, text = f'''보유효과 합산: 최종공격력 +{bonus:.1f}% (체육관 뱃지 위에 별도로 곱해져요){extra_line}{equip_line}''', font = ('맑은 고딕', 9, 'bold'), fg = '#1a4a8a', wraplength = 380, justify = 'left').pack(anchor = 'w', pady = (0, 10))
    earned = self.state.get('titles_earned', [])
    if not earned:
        None(body, text = '아직 획득한 칭호가 없어요. 무한성장미터에 도전해보세요!', font = ('맑은 고딕', 9), fg = '#888', wraplength = 380, justify = 'left').pack(pady = 20)
        return None
    earned = tk.Label(earned, (lambda t: if isinstance(t, dict):
    t.get('id')))
    for t in earned:
        row = None(body, relief = 'groove', bd = 1, cursor = 'hand2')
        row.pack(fill = 'x', pady = 3)
        equippable = _is_equippable_title(tid)
        if equippable:
            equippable
        is_equipped = title_equipped_id(self.state) == tid
        head = f'''🏆 {label}''' + ' 👑(장착 중)' if is_equipped else ''
        head_lbl = None(row, text = head, font = ('맑은 고딕', 9, 'bold'), anchor = 'w', justify = 'left', wraplength = 320, cursor = 'hand2')
        head_lbl.pack(anchor = 'w', padx = 6, pady = (4, 0))
        when_lbl = None
        if when:
            when_lbl = None(row, text = when, font = ('맑은 고딕', 7), fg = '#999', cursor = 'hand2')
            when_lbl.pack(anchor = 'w', padx = 6)
        effect_lbl = None(row, text = title_effect_text(tid), font = ('맑은 고딕', 7), fg = '#4a7a3a', justify = 'left', anchor = 'w', wraplength = 340, cursor = 'hand2')
        effect_lbl.pack(anchor = 'w', padx = 6, pady = (1, 0))
        for w_ in (row, head_lbl, effect_lbl) + (when_lbl,) if when_lbl else ():
            None(w_, (lambda label = label, tid = tid: None(tid, f'''🏆 {label}''')))
        (row, head_lbl, effect_lbl) + (when_lbl,) if when_lbl else ()
        if not equippable:
            continue
        btn_row = None(row)
        btn_row.pack(anchor = 'e', padx = 6, pady = (2, 4))
        if is_equipped:
            None(btn_row, text = '장착 해제', font = ('맑은 고딕', 8), command = (lambda : (None(), _refresh, None()))).pack(side = 'right')
            continue
        None(btn_row, text = '장착하기', font = ('맑은 고딕', 8), command = (lambda tid = tid: (None(), _refresh, None()))).pack(side = 'right')
    tk.Button
