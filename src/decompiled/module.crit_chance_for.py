# module.crit_chance_for
# source line 2844
# Recovered from bytecode; default argument values are not shown.

def crit_chance_for(entry):
    spd = entry.get('spd', 50)
    return max(10, min(25, 10 + 15 * (spd / 150)))
