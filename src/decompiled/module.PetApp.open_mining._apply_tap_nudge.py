# module.PetApp.open_mining._apply_tap_nudge
# source line 12134
# Recovered from bytecode; default argument values are not shown.

def _apply_tap_nudge(which):
    step = MINE_TAP_STEP * MINE_SECRET_SPEED_MULT if run['held']['ctrl'] else 1
    if which == 'right' and run['phase'] == 'go':
        run['progress'] = min(1, run['progress'] + step)
        None()
        if run['progress'] >= 1:
            None()
            return None
        return _redraw
    if None == 'left':
        if run['phase'] == 'return':
            run['progress'] = max(0, run['progress'] - step)
            None()
            if run['progress'] <= 0:
                None()
                return None
            return _redraw
        return None
