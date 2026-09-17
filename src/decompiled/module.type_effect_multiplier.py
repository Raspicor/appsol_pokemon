# module.type_effect_multiplier
# source line 3185
# Recovered from bytecode; default argument values are not shown.

def type_effect_multiplier(attacker_type, defender_types):
    if not attacker_type or defender_types:
        return 1
    mults = None
    for dt in defender_types:
        if dt in TYPE_SUPER_EFFECTIVE.get(attacker_type, ()):
            mults.append(TYPE_EFFECT_WEAK_MULT)
            continue
        if dt in TYPE_ORIG_IMMUNE.get(attacker_type, ()):
            mults.append(TYPE_EFFECT_IMMUNE_MULT)
            continue
        if dt in TYPE_NOT_VERY_EFFECTIVE.get(attacker_type, ()):
            mults.append(TYPE_EFFECT_RESIST_MULT)
            continue
        mults.append(1)
    if not mults:
        return 1
    return None(mults) / len(mults)
