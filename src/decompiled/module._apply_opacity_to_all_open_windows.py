# module._apply_opacity_to_all_open_windows
# source line 4494
# Recovered from bytecode; default argument values are not shown.

def _apply_opacity_to_all_open_windows(alpha):
    dead = []
    for w in _ALL_OPEN_TOPLEVELS:
        if w.winfo_exists():
            w.attributes('-alpha', alpha)
            continue
        dead.append(w)
    for w in dead:
        _ALL_OPEN_TOPLEVELS.remove(w)
    return None
    except Exception:
        dead.append(w)
        continue
    except ValueError:
        continue
