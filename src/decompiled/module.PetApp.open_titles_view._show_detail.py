# module.PetApp.open_titles_view._show_detail
# source line 14957
# Recovered from bytecode; default argument values are not shown.

def _show_detail(tid, label, extra_head):
    head = f'''{label}\n''' if label else ''
    txt = f'''{head}{extra_head}{title_effect_text(tid)}'''
    detail_var.set(txt)
    detail_frame.configure(text = '칭호 상세')
