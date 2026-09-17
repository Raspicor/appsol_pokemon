# module.PetApp._backfill_missing_titles
# source line 14866
# Recovered from bytecode; default argument values are not shown.

def _backfill_missing_titles(self):
    msgs = []
    best = self.state.get('inf_meter_best', { })
    max_best = 0
    for m in INF_METER_MODES:
        max_best = max(max_best, int(best.get(m, 0)))
    k = 1
    if k * INF_TITLE_EVERY <= max_best:
        msgs.extend(self._check_inf_recurring_title(k * INF_TITLE_EVERY))
        k += 1
        continue
    msgs.extend(self._check_gen_master_titles())
    msgs.extend(self._check_new_titles())
    if msgs:
        self.save_state()
    return msgs
    except Exception:
        continue
