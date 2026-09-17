# module.draw_infinite_stone_fallback
# source line 1801
# Recovered from bytecode; default argument values are not shown.

def draw_infinite_stone_fallback(size, broken):
    img = None('RGBA', (size, size), (0, 0, 0, 0))
    d = None(img)
    if not broken:
        d.ellipse([
            size * 0.12,
            size * 0.25,
            size * 0.88,
            size * 0.95], fill = (150, 140, 130, 255), outline = (90, 82, 74, 255), width = max(1, size // 30))
        d.ellipse([
            size * 0.3,
            size * 0.08,
            size * 0.75,
            size * 0.45], fill = (170, 160, 150, 255), outline = (90, 82, 74, 255), width = max(1, size // 35))
        return img
    rnd = None(42)
    for _ in range(6):
        cx = rnd.uniform(size * 0.15, size * 0.85)
        cy = rnd.uniform(size * 0.55, size * 0.9)
        r = rnd.uniform(size * 0.06, size * 0.14)
        d.ellipse([
            cx - r,
            cy - r,
            cx + r,
            cy + r], fill = (150, 140, 130, 255), outline = (90, 82, 74, 255), width = max(1, size // 40))
    ImageDraw.Draw.Random
    return img
