# module.PetApp._ask_dex_replace_choice._row
# source line 11260
# Recovered from bytecode; default argument values are not shown.

def _row(rnum, label, lv, r, color):
    None(table, text = label, font = ('맑은 고딕', 9, 'bold'), fg = color, width = 9, anchor = 'center').grid(row = rnum, column = 0)
    None(table, text = f'''Lv.{lv}''', width = 9, anchor = 'center').grid(row = rnum, column = 1)
    None(table, text = f'''+{r['atk_pct']:.1f}%''', width = 9, anchor = 'center').grid(row = rnum, column = 2)
    None(table, text = f'''+{r['def_pct']:.1f}%''', width = 9, anchor = 'center').grid(row = rnum, column = 3)
    None(table, text = f'''+{r['crit_pct']:.1f}%p''', width = 9, anchor = 'center').grid(row = rnum, column = 4)
