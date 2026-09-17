# module.PetApp.open_settings._limit_nick
# source line 18738
# Recovered from bytecode; default argument values are not shown.

def _limit_nick(*_a):
    v = nick_var.get()
    if len(v) > 8:
        nick_var.set(v[<TYPE: 58>
    ])
        return None
