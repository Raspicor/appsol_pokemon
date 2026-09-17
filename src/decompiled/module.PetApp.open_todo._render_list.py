# module.PetApp.open_todo._render_list
# source line 18661
# Recovered from bytecode; default argument values are not shown.

def _render_list():
    for w in list_inner.winfo_children():
        w.destroy()
    todos = self._todo_list()
    for None in :
        t = None
        if t.get('done'):
            continue

    , [], pending, t = todos, t
    for None in :
        t = None
        if not t.get('done'):
            continue

    , [], done, t = todos, t

    def _row(parent, t):
        '''groove'''
        row = None(parent, relief = 'groove', bd = 1, padx = 4, pady = 3)
        row.pack(fill = 'x', pady = 2)
        chk_var = None(value = bool(t.get('done')))
        None(row, variable = chk_var, command = (lambda : None(t))).pack(side = 'left')
        alarm_txt = ''
        if t.get('alarm_at'):
            alarm_txt = time.strftime + '%m/%d %H:%M'(time.localtime, None(t['alarm_at']))
            if t.get('alarm_fired'):
                alarm_txt += '(알림됨)'
        text_disp = t.get('text', '')
        if t.get('done'):
            text_disp = '✅ ' + text_disp
        None(row, text = text_disp + alarm_txt, font = ('맑은 고딕', 9), wraplength = 190, justify = 'left', anchor = 'w').pack(side = 'left', fill = 'x', expand = True, padx = (4, 4))
        None(row, text = '삭제', font = ('맑은 고딕', 7), command = (lambda : None(t))).pack(side = 'right')

    if not pending and done:
        None(list_inner, text = '할일이 없어요. 위에서 추가해보세요!', font = ('맑은 고딕', 8), fg = '#888').pack(pady = 10)
        return None
    None(list_inner, text = f'''◽ 미완료 ({len(pending)})''', font = ('맑은 고딕', 8, 'bold'), fg = '#1a4a8a').pack(anchor = 'w', pady = (2, 0))
    if not pending:
        None(list_inner, text = '(없음)', font = ('맑은 고딕', 8), fg = '#aaa').pack(anchor = 'w')
    for t in pending:
        None(list_inner, t)
    pending
    None(list_inner, text = f'''✅ 완료 ({len(done)})''', font = ('맑은 고딕', 8, 'bold'), fg = '#1a6b1a').pack(anchor = 'w', pady = (8, 0))
    if not done:
        None(list_inner, text = '(없음)', font = ('맑은 고딕', 8), fg = '#aaa').pack(anchor = 'w')
    for t in done:
        None(list_inner, t)
    done
    return None
