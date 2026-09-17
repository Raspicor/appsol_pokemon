# module._dir_from_vector
# source line 4061
# Recovered from bytecode; default argument values are not shown.

def _dir_from_vector(dx, dy):
    if abs(dx) < 0.01 and abs(dy) < 0.01:
        return None
    ang = math.atan2(None(-dy, dx)) % 360
    order = [
        spriteanim.DIR_RIGHT,
        spriteanim.DIR_UP_RIGHT,
        spriteanim.DIR_UP,
        spriteanim.DIR_UP_LEFT,
        spriteanim.DIR_LEFT,
        spriteanim.DIR_DOWN_LEFT,
        spriteanim.DIR_DOWN,
        spriteanim.DIR_DOWN_RIGHT]
    sector = int(((ang + 22.5) % 360) // 45) % 8
    return order[sector]
