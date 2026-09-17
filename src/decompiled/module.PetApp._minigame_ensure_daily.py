# module.PetApp._minigame_ensure_daily
# source line 5450
# Recovered from bytecode; default argument values are not shown.

def _minigame_ensure_daily(self):
    today = None('%Y-%m-%d')
    d = self.state.get('minigame_daily')
    if not isinstance(d, dict):
        d = { }
        self.state['minigame_daily'] = d
    if d.get('date') != today:
        d.clear()
        d.update(dict(DEFAULT_STATE['minigame_daily']))
        d['date'] = today
    return d
