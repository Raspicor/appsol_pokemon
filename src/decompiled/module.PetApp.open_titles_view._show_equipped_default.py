# module.PetApp.open_titles_view._show_equipped_default
# source line 14963
# Recovered from bytecode; default argument values are not shown.

def _show_equipped_default():
    eid = title_equipped_id(self.state)
    if eid:
        if not title_equipped_label(self.state):
            title_equipped_label(self.state)
        elabel = eid
        detail_var.set(f'''👑 {elabel}\n{title_effect_text(eid)}''')
        detail_frame.configure(text = '칭호 상세 (지금 장착 중)')
        return None
    None.set('지금 장착한 칭호가 없어요. 아래에서 마스터 칭호를 장착하거나,\n칭호를 눌러보면 여기에 상세 효과가 나와요.')
    detail_frame.configure(text = '칭호 상세')
