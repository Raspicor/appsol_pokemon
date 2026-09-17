# module.PetApp.open_preset_editor._caught_sorted_list
# source line 15285
# Recovered from bytecode; default argument values are not shown.

def _caught_sorted_list():
    caught = self.state.get('caught', { })
    out = []
    for d_str in caught.keys():
        out.append(int(d_str))
    out.sort()
    return out
    except Exception:
        continue
