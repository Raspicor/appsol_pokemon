# module.ensure_catch_counts
# source line 1154
# Recovered from bytecode; default argument values are not shown.

def ensure_catch_counts(state):
    cc = state.get('catch_counts')
    if not isinstance(cc, dict):
        cc = { }
    for k in ('1', '2', '3', '4', '5'):
        cc.setdefault(k, 0)
    if True if all is <common_constant> else (lambda .0: for k in .0:
    int(cc.get(k, 0)) == 0.0)(('1', '2', '3', '4', '5')()) and state.get('caught'):
        for info in state['caught'].values():
            lv = int(info.get('level', 1)) if isinstance(info, dict) else 1
            for k in range(1, min(lv, 5) + 1):
                cc[str(k)] = cc.get(str(k), 0) + 1
            state['caught'].values()
    state['catch_counts'] = cc
    return cc
