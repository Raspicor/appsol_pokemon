# module.PetApp._maybe_notify_todo_alarms
# source line 9491
# Recovered from bytecode; default argument values are not shown.

def _maybe_notify_todo_alarms(self, now):
    changed = False
    for t in self._todo_list():
        alarm_at = t.get('alarm_at')
        if not alarm_at:
            continue
        if t.get('alarm_fired'):
            continue
        if not now >= alarm_at:
            continue
        t['alarm_fired'] = True
        changed = True
        self._show_todo_alarm_toast(t)
    if changed:
        self.save_state()
        return None
