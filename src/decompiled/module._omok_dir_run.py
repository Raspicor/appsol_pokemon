# module._omok_dir_run
# source line 3728
# Recovered from bytecode; default argument values are not shown.

def _omok_dir_run(board, x, y, color, dx, dy, n):
    count = 1
    cy = y + dy
    cx = x + dx
    if  <= 0, cx or 0, cx < n:
        pass

    if  <= 0, cy or 0, cy < n:
        pass

    if board[cy][cx] == color:
        count += 1
        cy += dy
        continue
    if None if  <= 0, cx else None, 0, cx < n:
        None if  <= 0, cx else None, 0, cx < n
        if None if  <= 0, cy else None, 0, cy < n:
            None if  <= 0, cy else None, 0, cy < n
    cy = y - dy
    cx = x - dx
    if  <= 0, cx or 0, cx < n:
        pass
    else:
        board[cy][cx] is None
    if  <= 0, cy or 0, cy < n:
        pass
    else:
        board[cy][cx] is None
    if board[cy][cx] == color:
        count += 1
        cy -= dy
        continue
    if None if  <= 0, cx else board[cy][cx] is None, 0, cx < n:
        None if  <= 0, cx else board[cy][cx] is None, 0, cx < n
        if None if  <= 0, cy else None, 0, cy < n:
            None if  <= 0, cy else None, 0, cy < n
    return (count, int(open1) + int(open2))
