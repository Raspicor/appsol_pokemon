# module.PetApp.open_todo._add
# source line 18623
# Recovered from bytecode; default argument values are not shown.

def _add():
    val = entry.get().strip()
    if not val:
        return None
    item = {
        'popup_dur': 5,
        'alarm_fired': False,
        'alarm_at': None,
        'done': False,
        **val }
    if alarm_on_var.get():
    
        try:
            hh = int(hour_var.get())
            mm = int(min_var.get())
            now_t = None()
            target = None((now_t.tm_year, now_t.tm_mon, now_t.tm_mday, hh, mm, 0, 0, 0, -1))
            if time.time <= None():
                target += 86400
            item['alarm_at'] = target
            item['popup_dur'] = dur_var.get()
            self._todo_list().append(item)
            self.save_state()
            entry.delete(0, 'end')
            alarm_on_var.set(False)
            None()
            return None
        except Exception:
            mm = 0
            hh = 0
            continue
