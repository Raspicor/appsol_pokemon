# module.PetApp.open_mining._key_press._h
# source line 12185
# Recovered from bytecode; default argument values are not shown.

def _h(evt):
    was_held = run['held'].get(which, False)
    run['held'][which] = True
    if not which in ('right', 'left') and was_held:
        None(which)
    if which == 'right' and run['phase'] == 'go':
        status_var.set('→ 이동 중...')
        return None
    if _apply_tap_nudge == 'left':
        if run['phase'] == 'return':
            status_var.set('← 복귀 중...')
            return None
        return None
