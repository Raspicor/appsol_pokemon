# module.PetApp._build_combat_full._body_bar
# source line 10763
# Recovered from bytecode; default argument values are not shown.

def _body_bar(key, name, level, color):
    e = body_entry(ctx, key)
    bs = body_bs(ctx, key)
    type_mult = self.my_type_effect_mult(wild_types_full) if key == 'player' else type_effect_multiplier(pokedex_types(e)[0], wild_types_full) + self.companion_type_bonus_pct(wild_types_full) / 100
    name_var = None()
    None(bars, textvariable = name_var, anchor = 'w', fg = color, wraplength = 440, justify = 'left').pack(fill = 'x')
    pb = None(bars, length = 380, maximum = body_hp_max(ctx, key), value = body_hp(ctx, key))
    pb.pack(fill = 'x', pady = (0, 8))

    def refresh():
        '''active'''
        turn_mark = '▶ ' if ctx.get('active') == key else ''
        fainted = ' (기절)' if body_hp(ctx, key) <= 0 else ''
        name_var.set(f'''{turn_mark}{name} (Lv.{level}){fainted}  공{type_adjusted_atk_text(bs['atk'], type_mult)}/방{bs['def']}/크리{bs['crit']:.0f}%''')
    
        try:
            pb.configure(value = body_hp(ctx, key), maximum = body_hp_max(ctx, key))
            return None
        except Exception:
            return None


    None()
    return refresh
