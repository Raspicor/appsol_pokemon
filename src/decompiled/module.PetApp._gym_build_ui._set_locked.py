# module.PetApp._gym_build_ui._set_locked
# source line 17178
# Recovered from bytecode; default argument values are not shown.

def _set_locked(locked):
    state = 'disabled' if locked else 'normal'
    for b in (ult_btn, atk_btn, def_btn, give_btn):
        b.configure(state = state)
    return None
    except Exception:
        continue
