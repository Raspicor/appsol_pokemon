# module.PetApp._build_compact_battle._body_row
# source line 10163
# Recovered from bytecode; default argument values are not shown.

def _body_row(key, name, level, name_color):
    e = body_entry(ctx, key)
    bs = body_bs(ctx, key)
    type_mult = self.my_type_effect_mult(wild_types_) if key == 'player' else type_effect_multiplier(pokedex_types(e)[0], wild_types_) + self.companion_type_bonus_pct(wild_types_) / 100
    name_var = None()
    name_lbl = None(body, textvariable = name_var, bg = '#fff6e0', font = ('맑은 고딕', 9, 'bold'), fg = name_color, wraplength = 260, justify = 'center')
    name_lbl.pack(pady = (4, 0))
    None(body, text = f'''공 {type_adjusted_atk_text(bs['atk'], type_mult)}  /  방 {bs['def']}  /  크리 {bs['crit']:.0f}%''', bg = '#fff6e0', font = ('맑은 고딕', 8), fg = name_color).pack()
    pb = None(body, length = 210, maximum = body_hp_max(ctx, key), value = body_hp(ctx, key))
    pb.pack(pady = (0, 4))

    def refresh():
        '''active'''
        turn_mark = '▶ ' if ctx.get('active') == key else ''
        fainted = ' (기절)' if body_hp(ctx, key) <= 0 else ''
        name_var.set(f'''{turn_mark}{name} Lv.{level}{fainted}''')
    
        try:
            pb.configure(value = body_hp(ctx, key), maximum = body_hp_max(ctx, key))
            return None
        except Exception:
            return None


    None()
    return refresh
