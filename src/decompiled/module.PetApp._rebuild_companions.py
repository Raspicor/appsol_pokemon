# module.PetApp._rebuild_companions
# source line 6996
# Recovered from bytecode; default argument values are not shown.

def _rebuild_companions(self):
    for c in self.companions:
        c.destroy()
    self.companions = []
    hidden = (lambda .0: for x in .0:
    if not str(x).lstrip('-').isdigit():
    continueint(x).0)(self.state.get('party_hidden', [])())
    party = self.state.get('party', [])[:companion_slot_count(self.state)]
    for None in visible_party,:
        if not int(d) not in hidden:
            continue
    visible_party, = , []
    d = party, d
    mega_set = (lambda .0: for x in .0:
    int(x).0)(self.state.get('mega_party', [])())
    for self.state.get('caught', { }).get(str(d), { }).get('level', 1) in enumerate(visible_party):
        i = ()
        d = None
        if d in mega_set:
            d in mega_set
        is_mega = mega_companion_ready(d, self.state.get('caught', { }))
        self.companions.append(Companion(self, d, lv, slot_index = i, mega = is_mega))
    set
    self._rebuild_body2()
    self._apply_companion_ball_visibility()
    return None

    except Exception:
        None, set, None
        continue
    except Exception:
        None, set, None
        continue
