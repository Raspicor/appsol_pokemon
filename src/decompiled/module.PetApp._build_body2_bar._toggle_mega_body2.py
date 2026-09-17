# module.PetApp._build_body2_bar._toggle_mega_body2
# source line 7102
# Recovered from bytecode; default argument values are not shown.

def _toggle_mega_body2():
    if not mega_companion_ready(dex2, self.state.get('caught', { })):
        None('PikaPet', f'''이 개체는 아직 최고 레벨(Lv.{MAX_PLAYER_LEVEL})로 잡지 못했어요.\n최고 레벨 개체를 잡아서 2번 본체로 장착해보세요.''')
        return None
    self.state['mega_body2'] = not None(self.state.get('mega_body2'))
    self._rebuild_body2()
    self.save_state()
    None()
