# module.PetApp._start_omok_game._ai_turn
# source line 6819
# Recovered from bytecode; default argument values are not shown.

def _ai_turn():
    ctx['ai_job'] = None
    if ctx['closed'] or ctx['game_over']:
        return None

    try:
        mv = _omok_ai_pick_move(ctx['board'], ctx['difficulty'], 'B', 'A', n)
        if mv is None:
            return None
        x = ()
        y = None
        if ctx['board'][y][x] is not None:
            return None
        None(x, y, 'B')
        None(x, y, 'B')
        return None
    except Exception:
        continue
