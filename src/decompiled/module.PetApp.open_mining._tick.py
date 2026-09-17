# module.PetApp.open_mining._tick
# source line 12149
# Recovered from bytecode; default argument values are not shown.

def _tick():
    if not run['closed'] or win.winfo_exists():
        return None
    None()
    dt = 0.05
    speed = 1 / MINE_TRIP_SECONDS
    if run['held']['ctrl']:
        speed *= MINE_SECRET_SPEED_MULT
    moving = False
    arrived_now = False
    returned_now = False
    if run['phase'] == 'go' and run['held']['right']:
        moving = True
        run['progress'] = min(1, run['progress'] + speed * dt)
        if run['progress'] >= 1:
            arrived_now = True
        elif run['phase'] == 'return' and run['held']['left']:
            moving = True
            run['progress'] = max(0, run['progress'] - speed * dt)
            if run['progress'] <= 0:
                returned_now = True
    None(50, moving)
    None()
    if arrived_now:
        None()
    elif returned_now:
        None()
    run['tick_job'] = win.after(50, _tick)
