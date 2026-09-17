# module.PetApp._record_login_day
# source line 8098
# Recovered from bytecode; default argument values are not shown.

def _record_login_day(self):
    today = None('%Y-%m-%d')
    if self.state.get('last_login_day_recorded') != today:
        self.state['last_login_day_recorded'] = today
        self.state['login_days_count'] = int(self.state.get('login_days_count', 0)) + 1
        self.save_state()
        return None
    return time.strftime
