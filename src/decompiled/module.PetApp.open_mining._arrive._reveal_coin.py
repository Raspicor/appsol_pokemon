# module.PetApp.open_mining._arrive._reveal_coin
# source line 12065
# Recovered from bytecode; default argument values are not shown.

def _reveal_coin():
    if run['closed']:
        return None
    run['reward'] = None._roll_mine_reward()
    run['phase'] = 'return'
    status_var.set('🎒 뭔가 챙겼어요! ← 를 눌러서 돌아오세요!')
    None()
