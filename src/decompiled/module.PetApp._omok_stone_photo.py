# module.PetApp._omok_stone_photo
# source line 6485
# Recovered from bytecode; default argument values are not shown.

def _omok_stone_photo(self, color_key, size):
    canvas = None('RGBA', (size, size), (0, 0, 0, 0))
    d = None(canvas)

    try:
        d.ellipse([
            1,
            1,
            size - 2,
            size - 2], fill = fill, outline = outline, width = 2)
        hr = max(2, size // 6)
        hx = size * 0.32
        hy = size * 0.3
        d.ellipse([
            hx - hr,
            hy - hr,
            hx + hr,
            hy + hr], fill = highlight)
        return None(canvas)
    except Exception:
        continue
