# module.PetApp.open_mining._arrive
# source line 12058
# Recovered from bytecode; default argument values are not shown.

def _arrive():
    run['phase'] = 'arrived'
    status_var.set('🎉 도착! 코인을 캐는 중... (얼마인지는 돌아가면 알 수 있어요)')
    None()

    def _reveal_coin():
        '''closed'''
        if run['closed']:
            return None
        run['reward'] = None._roll_mine_reward()
        run['phase'] = 'return'
        status_var.set('🎒 뭔가 챙겼어요! ← 를 눌러서 돌아오세요!')
        None()

    win.after(700, _reveal_coin)
