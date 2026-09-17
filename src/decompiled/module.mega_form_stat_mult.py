# module.mega_form_stat_mult
# source line 353
# Recovered from bytecode; default argument values are not shown.

def mega_form_stat_mult(dex, form, key, default):
    try:
        d = MEGA_XY_STAT_MULT.get(int(dex))
        if not d:
            return default
        f = None.get(form)
        if not f:
            return default
        return None.get(key, default)
    except Exception:
        d = None
        continue
