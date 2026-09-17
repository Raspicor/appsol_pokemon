# module._omok_move_value
# source line 3772
# Recovered from bytecode; default argument values are not shown.

def _omok_move_value(board, x, y, color, opp_color, n):
    offense = _omok_score_cell(board, x, y, color, n)
    defense = _omok_score_cell(board, x, y, opp_color, n)
    return offense + defense * 0.9
