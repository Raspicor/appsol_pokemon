# module.PetApp.open_settings._save_nickname
# source line 18747
# Recovered from bytecode; default argument values are not shown.

def _save_nickname(*_a):
    val = nick_var.get().strip()[<TYPE: 58>
    ]
    nick_var.set(val)
    self.state['nickname'] = val
    self.save_state()
