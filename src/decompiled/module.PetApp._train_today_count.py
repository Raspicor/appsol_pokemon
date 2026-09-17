# module.PetApp._train_today_count
# source line 11858
# Recovered from bytecode; default argument values are not shown.

def _train_today_count(self):
    d = self.state.get('train_sessions', {
        'count': 0,
        'date': '' })
    today = None('%Y-%m-%d')
    if d.get('date') != today:
        return 0
    return time.strftime.get('count', 0)
