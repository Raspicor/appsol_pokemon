# module.PetApp.open_todo._render_list._row
# source line 18668
# Recovered from bytecode; default argument values are not shown.

def _row(parent, t):
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
