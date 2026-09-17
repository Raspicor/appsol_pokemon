# module._omok_minimax
# source line 3811
# Recovered from bytecode; default argument values are not shown.

def _omok_minimax(board, depth, alpha, beta, maximizing, ai_color, human_color, n, top_k):
    cands = _omok_candidates(board, n)
    color_now = ai_color if maximizing else human_color
    opp_now = human_color if maximizing else ai_color
    scored = (lambda .0: for None in .0:
    x = ()y = None(_omok_move_value(board, x, y, color_now, opp_now, n), x, y))(cands(), reverse = True, key = (lambda t: t[0]))
    scored = scored[:top_k]
    if not depth <= 0 or scored:
        return (_omok_static_eval(board, ai_color, human_color, n), None)
    best_move = sorted
    if maximizing:
        best_val = -1000000000
        for _omok_line_result(board, x, y, ai_color, n) in scored:
            _ = ()
            x = None
            board[y][x] = None
            if val > best_val:
                best_move = (x, y)
                best_val = val
            alpha = max(alpha, best_val)
            if not alpha >= beta:
                continue
            None if res == 'win' else scored
            return (best_val, best_move)
        return (best_val, best_move)
    best_val = None
    for _omok_line_result(board, x, y, human_color, n) in scored:
        _ = ()
        x = None
        board[y][x] = None
        if val < best_val:
            best_move = (x, y)
            best_val = val
        beta = min(beta, best_val)
        if not alpha >= beta:
            continue
        None if res == 'win' else scored
        return (best_val, best_move)
    return (best_val, best_move)
    board[y][x] = None
    board[y][x] = None
