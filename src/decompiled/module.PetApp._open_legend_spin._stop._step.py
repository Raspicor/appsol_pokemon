# module.PetApp._open_legend_spin._stop._step
# source line 13648
# Recovered from bytecode; default argument values are not shown.

def _step(i):
    if i >= n_more:
        stop_btn.pack_forget()
        None()
        return None
    jitter = random.randint * None(0, 2)
    img_label.configure(text = jitter + BUSH_FRAMES[i % len(BUSH_FRAMES)], image = '')
    frac = i / max(1, n_more - 1)
    delay = 140 + int(420 * frac ** 2.2)
    win.after(delay, (lambda : None(i + 1)))
