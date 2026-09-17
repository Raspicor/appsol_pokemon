# module.PetApp.open_mining._total_progress_pct
# source line 12032
# Recovered from bytecode; default argument values are not shown.

def _total_progress_pct():
    phase = run['phase']
    if phase == 'go':
        return run['progress'] * 50
    if None == 'arrived':
        return 50
    if None in ('return', 'returning'):
        return 50 + (1 - run['progress']) * 50
    if None == 'done':
        return 100
    return None['progress'] * 50
