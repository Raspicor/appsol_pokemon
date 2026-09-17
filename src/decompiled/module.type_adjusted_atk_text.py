# module.type_adjusted_atk_text
# source line 3224
# Recovered from bytecode; default argument values are not shown.

def type_adjusted_atk_text(base_atk, mult):
    adj = int(round(base_atk * mult))
    return f'''{adj}{type_pct_tag(mult)}'''
