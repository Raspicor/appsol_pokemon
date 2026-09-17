# module.PetApp._build_compact_battle._body_row.refresh
# source line 10180
# Recovered from bytecode; default argument values are not shown.

def refresh():
    turn_mark = '▶ ' if ctx.get('active') == key else ''
    fainted = ' (기절)' if body_hp(ctx, key) <= 0 else ''
    name_var.set(f'''{turn_mark}{name} Lv.{level}{fainted}''')

    try:
        pb.configure(value = body_hp(ctx, key), maximum = body_hp_max(ctx, key))
        return None
    except Exception:
        return None
