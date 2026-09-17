# module._omok_candidates
# source line 3779
# Recovered from bytecode; default argument values are not shown.

def _omok_candidates(board, n, radius):
    for None in :
        for None in range(n):
            x = None
            if board[y][x] is None:
                continue

    , [], occupied = range(n), y, x
    y = None
    x = None
    if not occupied:
        return [
            (n // 2, n // 2)]
    cand = None()
    for None in occupied:
        ox = ()
        oy = None
        for None in range(-radius, radius + 1):
            for None in range(-radius, radius + 1):
                y = oy + dy
                x = ox + dx
                if  <= 0, x:
                    if not 0, x < n:
                        continue
                
                    if  <= 0, y:
                        if not 0, y < n:
                            continue
                    
                        if board[y][x] is not None:
                            continue
                cand.add((x, y))
    if cand:
        return list(cand)
    for None in :
        for None in range(n):
            x = None
            if board[y][x] is not None:
                continue

    return x, y
