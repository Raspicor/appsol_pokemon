# module.PetApp.open_game_quiz._tick_timer
# source line 6255
# Recovered from bytecode; default argument values are not shown.

def _tick_timer():
    if ctx['closed'] or ctx['answered']:
        return None
    if ctx['remaining'] <= 0:
        timer_var.set('시간 초과!')
        None(None)
        return None
    None.set(f'''남은 시간: {ctx['remaining']}초''')
    win.after(1000, _tick_timer) = None
