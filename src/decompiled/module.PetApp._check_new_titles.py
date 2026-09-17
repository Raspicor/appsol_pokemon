# module.PetApp._check_new_titles
# source line 14810
# Recovered from bytecode; default argument values are not shown.

def _check_new_titles(self):
    msgs = []
    for entry in NEW_TITLE_TABLE:
        tid = entry['id']
        already = tid in _earned_ids(self.state)
        if already:
            continue
        ok = entry['cond'](None(self.state))
        if not ok:
            continue
        msg = self._award_title(tid, entry['label'])
        if not msg:
            continue
        msgs.append(msg)
    return msgs
    except Exception:
        ok = False
        continue
