# module.newly_completed_gens
# source line 1274
# Recovered from bytecode; default argument values are not shown.

def newly_completed_gens(state):
    shown = state.get('gen_cert_shown')
    if not isinstance(shown, list):
        shown = []
    out = []
    for None in GEN_COMPLETE_INFO.items():
        gen = ()
        info = None
        if gen in shown:
            continue
        if None(state):
            out.append(gen)
            continue
    GEN_COMPLETE_INFO.items()
    return out
    except Exception:
        continue
