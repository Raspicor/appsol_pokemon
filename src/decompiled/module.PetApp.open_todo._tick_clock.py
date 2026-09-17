# module.PetApp.open_todo._tick_clock
# source line 18552
# Recovered from bytecode; default argument values are not shown.

def _tick_clock():
    if not win.winfo_exists():
        return None
    time.strftime(None('%Y-%m-%d %H:%M:%S'))
    win.after(1000, _tick_clock)
