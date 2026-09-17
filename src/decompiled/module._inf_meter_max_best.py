# module._inf_meter_max_best
# source line 2228
# Recovered from bytecode; default argument values are not shown.

def _inf_meter_max_best(state):
    best = state.get('inf_meter_best', { })
    m = 0
    for mode in INF_METER_MODES:
        m = max(m, int(best.get(mode, 0)))
    return m
    except Exception:
        continue
