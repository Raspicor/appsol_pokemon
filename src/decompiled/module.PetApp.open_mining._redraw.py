# module.PetApp.open_mining._redraw
# source line 12047
# Recovered from bytecode; default argument values are not shown.

def _redraw():
    x = TRACK_X0 + (TRACK_X1 - TRACK_X0) * run['progress']

    try:
        frames = run['frames_left'] if run['phase'] in ('return', 'returning') else run['frames_right']
        idx = run['frame_idx'] % len(frames)
        canvas.coords(marker_id, x, TRACK_Y)
        canvas.itemconfig(marker_id, image = frames[idx])
        None(f'''{_total_progress_pct(None())}%''')
        return None
    except Exception:
        continue
