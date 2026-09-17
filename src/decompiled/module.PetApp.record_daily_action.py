# module.PetApp.record_daily_action
# source line 8108
# Recovered from bytecode; default argument values are not shown.

def record_daily_action(self):
    today = None('%Y-%m-%d')
    d = self.state.setdefault('daily_action_count', {
        'credited': False,
        'count': 0,
        'date': today })
    if d.get('date') != today:
        if not d.get('count', 0) >= DAILY_QUOTA and d.get('credited', False):
            self.state['quota_days_done'] = self.state.get('quota_days_done', 0) + 1
            self.state['daily_quest_lifetime_days'] = int(self.state.get('daily_quest_lifetime_days', 0)) + 1
        d['date'] = today
        d['count'] = 0
        d['credited'] = False
    d['count'] = d.get('count', 0) + 1
    if d['count'] >= DAILY_QUOTA:
        if not d.get('credited', False):
            d['credited'] = True
            self.state['quota_days_done'] = self.state.get('quota_days_done', 0) + 1
            self.state['daily_quest_lifetime_days'] = int(self.state.get('daily_quest_lifetime_days', 0)) + 1
            return None
        return time.strftime
    return time.strftime
