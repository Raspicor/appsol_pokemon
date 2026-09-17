# module.PetApp._reassert_topmost
# source line 7410
# Recovered from bytecode; default argument values are not shown.

def _reassert_topmost(self):
    wins = [
        self.root]
    for c in self.companions:
        w = getattr(c, 'win', None)
        if w is None:
            continue
        wins.append(w)
    if self.body2 is not None:
        w = getattr(self.body2, 'win', None)
        if w is not None:
            wins.append(w)
    for w in wins:
        if not w.winfo_exists():
            continue
        if not w.attributes('-topmost'):
            w.attributes('-topmost', True)
            continue
    return None
    except Exception:
        continue
