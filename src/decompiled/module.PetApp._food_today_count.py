# module.PetApp._food_today_count
# source line 11891
# Recovered from bytecode; default argument values are not shown.

def _food_today_count(self):
    d = self.state.get('food_sessions', {
        'count': 0,
        'date': '' })
    if time.strftime != None('%Y-%m-%d'):
        return 0
    return d.get('date').get('count', 0)
