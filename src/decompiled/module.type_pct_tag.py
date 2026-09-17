# module.type_pct_tag
# source line 3216
# Recovered from bytecode; default argument values are not shown.

def type_pct_tag(mult):
    pct = (mult - 1) * 100
    if abs(pct) < 4:
        return ''
    return f'''{pct:+.0f}%)'''
