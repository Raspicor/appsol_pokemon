# module.PetApp._build_combat_full._body_bar.refresh
# source line 10775
# Recovered from bytecode; default argument values are not shown.

def refresh():
    turn_mark = '▶ ' if ctx.get('active') == key else ''
    fainted = ' (기절)' if body_hp(ctx, key) <= 0 else ''
    name_var.set(f'''{turn_mark}{name} (Lv.{level}){fainted}  공{type_adjusted_atk_text(bs['atk'], type_mult)}/방{bs['def']}/크리{bs['crit']:.0f}%''')

    try:
        pb.configure(value = body_hp(ctx, key), maximum = body_hp_max(ctx, key))
        return None
    except Exception:
        return None
