# module._omok_line_result
# source line 3747
# Recovered from bytecode; default argument values are not shown.

def _omok_line_result(board, x, y, color, n):
    dirs = [
        (1, 0),
        (0, 1),
        (1, 1),
        (1, -1)]
    overline = False
    for None in dirs:
        dx = ()
        dy = None
        count = ()
        _open_ends = _omok_dir_run(board, x, y, color, dx, dy, n)
        if count == 5:
            dirs
            return 'win'
        if not dirs >= 6:
            continue
    if overline:
        return 'overline'
