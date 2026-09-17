# module._omok_score_cell
# source line 3761
# Recovered from bytecode; default argument values are not shown.

def _omok_score_cell(board, x, y, color, n):
    dirs = [
        (1, 0),
        (0, 1),
        (1, 1),
        (1, -1)]
    total = 0
    for total += _OMOK_PATTERN_SCORE.get((capped, open_ends), 0) in dirs:
        dx = ()
        dy = None
        count = ()
        open_ends = _omok_dir_run(board, x, y, color, dx, dy, n)
    return total
