# module.PetApp._open_legend_spin._tick_spin
# source line 13578
# Recovered from bytecode; default argument values are not shown.

def _tick_spin():
    if spin_state['phase'] != 'spin':
        return None
    jitter = random.randint * None(0, 2)
    img_label.configure(text = jitter + BUSH_FRAMES[spin_state['idx'] % len(BUSH_FRAMES)], image = '')
    win.after(140, _tick_spin) = None
