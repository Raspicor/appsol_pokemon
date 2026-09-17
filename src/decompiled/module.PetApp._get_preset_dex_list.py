# module.PetApp._get_preset_dex_list
# source line 15133
# Recovered from bytecode; default argument values are not shown.

def _get_preset_dex_list(self, category):
    out = []
    for d in self._get_preset_slots(category):
        if d is None:
            continue
        out.append(int(d))
    if out:
        return out
    cap = None._preset_cap(category)
    return list(self.state.get('party', []))[:cap]
    except Exception:
        continue
