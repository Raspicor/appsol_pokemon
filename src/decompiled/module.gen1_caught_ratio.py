# module.gen1_caught_ratio
# source line 1212
# Recovered from bytecode; default argument values are not shown.

def gen1_caught_ratio(state):
    caught = state.get('caught', { })
    n = (lambda .0: for d in .0:
    if not str(d) in caught:
    continue1.0)(range(1, 152)())
    return n / 151
