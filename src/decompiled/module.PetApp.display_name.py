# module.PetApp.display_name
# source line 5424
# Recovered from bytecode; default argument values are not shown.

def display_name(self):
    if not self.state.get('nickname'):
        self.state.get('nickname')
    nick = ''.strip()
    if nick:
        base = nick
    else:
        conf = self.stage_conf()
        base = conf.get('kr', '내 포켓몬')
        if not self.state.get('mega_evolved') and self.state.get('custom_body_dex'):
            mega_name = self.mega_display_name_for()
            if mega_name:
                base = mega_name
    title_label = title_equipped_label(self.state)
    if title_label:
        return f'''《{title_label}》{base}'''
