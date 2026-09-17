# module.PetApp._mine_bump_today
# source line 11880
# Recovered from bytecode; default argument values are not shown.

def _mine_bump_today(self):
    today = None('%Y-%m-%d')
    d = self.state.setdefault('mine_sessions', {
        'count': 0,
        'date': today })
    if d.get('date') != today:
        d['date'] = today
        d['count'] = 0
    d['count'] = d.get('count', 0) + 1
    self.state['mine_lifetime_plays'] = int(self.state.get('mine_lifetime_plays', 0)) + 1
