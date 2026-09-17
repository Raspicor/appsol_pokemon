# module.PetApp._mine_today_count
# source line 11874
# Recovered from bytecode; default argument values are not shown.

def _mine_today_count(self):
    d = self.state.get('mine_sessions', {
        'count': 0,
        'date': '' })
    if time.strftime != None('%Y-%m-%d'):
        return 0
    return d.get('date').get('count', 0)
