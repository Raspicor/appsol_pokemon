# module.PetApp.open_titles_view._refresh_list_tab._on_click
# source line 15081
# Recovered from bytecode; default argument values are not shown.

def _on_click(tid, label, cond, owned):
    head_txt = f'''{'✅ 보유 중' if owned else '🔒 아직 미보유'} - {label}\n조건: {cond}\n'''
    None(tid, '', extra_head = head_txt)
