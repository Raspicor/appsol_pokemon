# module._omok_find_immediate_win
# source line 3865
# Recovered from bytecode; default argument values are not shown.

def _omok_find_immediate_win(board, cands, color, n):
    for _omok_line_result(board, x, y, color, n) in cands:
        x = ()
        y = None
        board[y][x] = None
        if not res == 'win':
            continue
    
        return cands, (x, y)
