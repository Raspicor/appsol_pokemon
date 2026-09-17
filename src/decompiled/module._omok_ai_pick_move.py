# module._omok_ai_pick_move
# source line 3878
# Recovered from bytecode; default argument values are not shown.

def _omok_ai_pick_move(board, difficulty, ai_color, human_color, n):
    cands = _omok_candidates(board, n)
    if not cands:
        return None
    if None == '완전쉬움':
        if None() < 0.2:
            mv = _omok_find_immediate_win(board, cands, ai_color, n)
            if mv:
                return mv
            if None() < 0.2:
                mv = _omok_find_immediate_win(board, cands, human_color, n)
                if mv:
                    return mv
                return None(cands)
            mv = random.random.random(board, cands, ai_color, n)
            if mv:
                return mv
            mv = None(board, cands, human_color, n)
            if mv:
                return mv
        
            def _scored_moves():
                return (lambda .0: for None in .0:
    x = ()y = None(_omok_move_value(board, x, y, ai_color, human_color, n), x, y))(cands(), reverse = True, key = (lambda t: t[0]))

            if difficulty == '쉬움':
                scored = None()
                top = scored[<TYPE: 58>
    ] if len(scored) >= 6 else scored
                _ = ()
                x = None(top)
                return (x, y)
            if None == '보통':
                scored[<TYPE: 58>
    ] if len(scored) >= 3 else scored = None()
                _ = ()
                x = None(top)
                return (x, y)
            if None == '어려움':
                top_k = 8
                depth = 2
            elif difficulty == '극악':
                top_k = 8
                depth = 3
            else:
                top_k = 6
                depth = 4
    for None in :
        row = None

    , [], board_copy, row = board, row

    try:
        (_, best) = _omok_minimax(board_copy, depth, -1000000000, 1000000000, True, ai_color, human_color, n, top_k)
        if best is None:
            scored = None()
            best = random.choice if scored else None(cands)
        if difficulty == '극악' and None() < 0.1:
            scored = None()
            if len(scored) >= 2:
                best = (scored[1][1], scored[1][2])
        return best
    
    except Exception:
        None = None
        continue
