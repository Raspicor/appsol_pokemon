# module.PetApp._open_legend_spin._stop
# source line 13635
# Recovered from bytecode; default argument values are not shown.

def _stop():
    if spin_state['phase'] != 'spin':
        return None
    spin_state['phase'] = None
    if spin_state['job'] is not None:
    
        try:
            win.after_cancel(spin_state['job'])
            spin_state['job'] = None
            stop_btn.configure(state = tk.DISABLED, text = '멈추는 중...')
            n_more = None(6, 9)
        
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

            None(0)
            return None
        except Exception:
            continue
