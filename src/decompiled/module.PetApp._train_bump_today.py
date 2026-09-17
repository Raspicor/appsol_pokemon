# module.PetApp._train_bump_today
# source line 11865
# Recovered from bytecode; default argument values are not shown.

def _train_bump_today(self):
    today = None('%Y-%m-%d')
    d = self.state.setdefault('train_sessions', {
        'count': 0,
        'date': today })
    if d.get('date') != today:
        d['date'] = today
        d['count'] = 0
    d['count'] = d.get('count', 0) + 1
