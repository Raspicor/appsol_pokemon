# module.eevee_friendship_ready
# source line 1237
# Recovered from bytecode; default argument values are not shown.

def eevee_friendship_ready(state):
    et = state.get('element_train', {
        'electric': 0,
        'water': 0,
        'fire': 0 })
    e = et.get('electric', 0)
    w = et.get('water', 0)
    f = et.get('fire', 0)
    if tied:
        tied
    return state.get('affection', 50) >= EEVEE_FRIENDSHIP_AFFECTION_MIN
