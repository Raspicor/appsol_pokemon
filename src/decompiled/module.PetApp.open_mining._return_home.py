# module.PetApp.open_mining._return_home
# source line 12075
# Recovered from bytecode; default argument values are not shown.

def _return_home():
    run['phase'] = 'returning'
    status_var.set('두구두구...')
    steps = {
        'n': 0 }

    def _drumroll():
        '''closed'''
        if run['closed']:
            return None
        status_var.set('두구두구' + '.' * (steps['n'] % 4))
        if steps['n'] < 5:
            win.after(280, _drumroll)
            return None
        if not None['reward']:
            None['reward']
        0 = None
        self._earn_gold(reward, source = 'mine')
        self._mine_bump_today()
        self.save_state()
        run['phase'] = 'done'
        status_var.set(f'''💰 얼마 벌어왔어요! +{reward}골드! (오늘 {self._mine_today_count()}/{MINE_MAX_PER_DAY}회 사용)''')
        None()

    win.after(280, _drumroll)
