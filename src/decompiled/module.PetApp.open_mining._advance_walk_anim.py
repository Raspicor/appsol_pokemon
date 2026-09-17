# module.PetApp.open_mining._advance_walk_anim
# source line 12018
# Recovered from bytecode; default argument values are not shown.

def _advance_walk_anim(dt_ms, moving):
    if not moving:
        run['frame_idx'] = 0
        run['frame_elapsed'] = 0
        return None
    durs = None['frame_durations']
    n = len(durs)
    0 = None
    if guard < 10:
        if run['frame_elapsed'] >= durs[run['frame_idx'] % n]:
            (run['frame_idx'] + 1) % n = None
            guard += 1
            continue
        return None
