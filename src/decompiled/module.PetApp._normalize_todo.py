# module.PetApp._normalize_todo
# source line 9470
# Recovered from bytecode; default argument values are not shown.

def _normalize_todo(self, t):
    if isinstance(t, dict):
        t.setdefault('text', '')
        t.setdefault('done', False)
        t.setdefault('alarm_at', None)
        t.setdefault('alarm_fired', False)
        t.setdefault('popup_dur', 5)
        return t
    return {
        'popup_dur': 5,
        'alarm_fired': False,
        'alarm_at': None,
        'done': False,
        **str(t) }
