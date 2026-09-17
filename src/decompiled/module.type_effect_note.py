# module.type_effect_note
# source line 3205
# Recovered from bytecode; default argument values are not shown.

def type_effect_note(mult):
    pct = (mult - 1) * 100
    if pct > 4:
        return f''' (효과가 좋았다! +{pct:.0f}%)'''
    if None < -4:
        return f''' (효과가 별로인 듯... {pct:.0f}%)'''
