# module.PetApp.open_mining._key_release
# source line 12200
# Recovered from bytecode; default argument values are not shown.

def _key_release(which):
    def _h(evt = None):
        run['held'][which] = False
        if which == 'right' and run['phase'] == 'go' and run['progress'] < 1:
            status_var.set('멈췄어요. → 를 다시 눌러서 이동하세요!')
            return None
        if None == 'left':
            if run['phase'] == 'return':
                if run['progress'] > 0:
                    status_var.set('멈췄어요(뭔가 챙긴 채). ← 를 다시 눌러서 이동하세요!')
                    return None
                return None
            return None

    return _h
