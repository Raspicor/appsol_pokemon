# module.play_sprite_action._step
# source line 3607
# Recovered from bytecode; default argument values are not shown.

def _step(i):
    try:
        if not label.winfo_exists():
            return None
        frame = aset.frame(action_name, i, dir_idx)
        if frame is not None:
            frame = frame.convert('RGBA')
            if frame_post:
            
                try:
                    frame = None(frame)
                    s = target_h / max(1, frame.height)
                    frame = frame.resize((max(8, int(frame.width * s)), max(8, int(frame.height * s))), Image.NEAREST)
                    tkimg = None(frame)
                    label.image = tkimg
                    label.configure(image = tkimg)
                    nxt = i + 1
                    if nxt < n:
                        dur = max(1, aset.duration_of(action_name, i)) * ANIM_TICK_MS
                    
                        try:
                            win.after(dur, (lambda : None(nxt)))
                            return None
                            if on_done:
                                None()
                                return None
                            return ImageTk.PhotoImage
                            except Exception:
                                return None
                            except Exception:
                                continue
                        except Exception:
                            frame_post
                            return None
