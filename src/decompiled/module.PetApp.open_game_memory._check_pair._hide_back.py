# module.PetApp.open_game_memory._check_pair._hide_back
# source line 6132
# Recovered from bytecode; default argument values are not shown.

def _hide_back():
    if ctx['closed']:
        return None
    for idx in (None, i2):
        btn = ctx['buttons'].get(idx)
        if btn is None:
            continue
        btn.configure(image = back_img)
    ctx['revealed'] = []
    ctx['locked'] = False
    return None
    except Exception:
        continue
