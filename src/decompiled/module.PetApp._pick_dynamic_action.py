# module.PetApp._pick_dynamic_action
# source line 4872
# Recovered from bytecode; default argument values are not shown.

def _pick_dynamic_action(self, candidates):
    aset = self.anim_sets.get(self.stage_conf()['id'])
    if aset is None:
        return None
    for name in None:
        if aset.has(name):
            if aset.n_frames(name) > 0:
            
                return None, name
    return None
    except Exception:
        continue
