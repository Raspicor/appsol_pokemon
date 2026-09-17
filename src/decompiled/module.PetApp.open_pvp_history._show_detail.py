# module.PetApp.open_pvp_history._show_detail
# source line 17964
# Recovered from bytecode; default argument values are not shown.

def _show_detail(entry):
    dwin = None(win)
    dwin.title('대결 상세')

    try:
        dwin.attributes('-topmost', True)
        resolve_species_win(dwin, 340, 380)
        db = None(dwin, padx = 12, pady = 10)
        db.pack(fill = 'both', expand = True)
        result = entry.get('result', '')
        if result == '승리':
            pass
        elif result == '패배':
            pass
    
        color = '#666'
        None(db, text = f'''상대: {entry.get('opponent', '상대')}''', font = ('맑은 고딕', 10, 'bold')).pack(anchor = 'w')
        None(db, text = entry.get('when', ''), font = ('맑은 고딕', 8), fg = '#888').pack(anchor = 'w')
        None(db, text = f'''결과: {result}''', font = ('맑은 고딕', 10, 'bold'), fg = color).pack(anchor = 'w', pady = (4, 10))
        None(db, text = '🔵 내 포켓몬', font = ('맑은 고딕', 9, 'bold'), fg = '#1a4a8a').pack(anchor = 'w')
        if not entry.get('my_party'):
            entry.get('my_party')
        my_list = [
            '(이 기록엔 없음)']
        None(db, text = ', '.join(my_list), font = ('맑은 고딕', 9), wraplength = 300, justify = 'left').pack(anchor = 'w', pady = (0, 10))
        None(db, text = '🔴 상대 포켓몬', font = ('맑은 고딕', 9, 'bold'), fg = '#a03030').pack(anchor = 'w')
        if not entry.get('opp_party'):
            entry.get('opp_party')
        opp_list = [
            '(이 기록엔 없음)']
        None(db, text = ', '.join(opp_list), font = ('맑은 고딕', 9), wraplength = 300, justify = 'left').pack(anchor = 'w', pady = (0, 10))
        None(db, text = '닫기', command = dwin.destroy).pack()
        self._add_opacity_control(dwin)
        return None
    except Exception:
        continue
