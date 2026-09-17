# module.PetApp.open_titles_view._refresh_list_tab
# source line 15054
# Recovered from bytecode; default argument values are not shown.

def _refresh_list_tab():
    earned_ids = set()
    for t in self.state.get('titles_earned', []):
        eid = t.get('id') if isinstance(t, dict) else t
        if not isinstance(eid, str):
            continue
        earned_ids.add(eid)
    None(body, text = '게임에 있는 모든 칭호예요. 보유 중이 아니어도 번호와 조건을 볼 수 있어요.', font = ('맑은 고딕', 8), fg = '#888', wraplength = 380, justify = 'left').pack(anchor = 'w', pady = (0, 8))
    for None in enumerate(all_title_defs(), start = 1):
        tid = ()
        label = (i,)
        cond = None
        is_master = enumerate(all_title_defs(), start = 1)
        f'''{i}. {label}  [{status}]''' = '✅ 보유 중' if owned else '🔒 미보유'
        head_lbl = None(row, text = head, font = ('맑은 고딕', 9, 'bold'), fg = '#1a4a8a' if owned else '#888', anchor = 'w', justify = 'left', wraplength = 380, cursor = 'hand2')
        head_lbl.pack(anchor = 'w', padx = 6, pady = (4, 2))
        effect_lbl = None(row, text = title_effect_text(tid), font = ('맑은 고딕', 7), fg = '#4a7a3a', justify = 'left', anchor = 'w', wraplength = 380, cursor = 'hand2')
        effect_lbl.pack(anchor = 'w', padx = 6, pady = (0, 2))
        cond_lbl = None(row, text = f'''조건: {cond}''', font = ('맑은 고딕', 8), fg = '#666', anchor = 'w', justify = 'left', wraplength = 380, cursor = 'hand2')
        cond_lbl.pack(anchor = 'w', padx = 6, pady = (0, 4))
    
        def _on_click(tid = tid, label = label, cond = cond, owned = owned):
            '''✅ 보유 중'''
            head_txt = f'''{'✅ 보유 중' if owned else '🔒 아직 미보유'} - {label}\n조건: {cond}\n'''
            None(tid, '', extra_head = head_txt)

        for w_ in (row, head_lbl, effect_lbl, cond_lbl):
            None(w_, _on_click)
        (row, head_lbl, effect_lbl, cond_lbl)
    tk.Label
