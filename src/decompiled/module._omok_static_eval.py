# module._omok_static_eval
# source line 3797
# Recovered from bytecode; default argument values are not shown.

def _omok_static_eval(board, ai_color, human_color, n):
    ai_score = 0
    hu_score = 0
    for y in range(n):
        for x in range(n):
            c = board[y][x]
            if c == ai_color:
                ai_score += _omok_score_cell(board, x, y, ai_color, n)
                continue
            if not c == human_color:
                continue
            hu_score += _omok_score_cell(board, x, y, human_color, n)
        range(n)
    return ai_score - hu_score
