# module.add_level_glow
# source line 3543
# Recovered from bytecode; default argument values are not shown.

def add_level_glow(img, level):
    if level or level < 1:
        return img
    img = None.convert('RGBA')
    pad = 5 + int(level) * 3
    w = ()
    h = img.size
    LEVEL_GLOW_COLORS.get(int(level), (255, 255, 255)) = None('RGBA', (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    glow = None('RGBA', canvas.size, (0, 0, 0, 0))
    gd = None(glow)
    rings = 3
    for i in range(rings):
        rr = pad - i * 2
        if rr <= 0:
            continue
        alpha = max(15, 70 + int(level) * 12 - i * 22)
        gd.ellipse([
            pad - rr,
            pad - rr,
            w + pad + rr,
            h + pad + rr], outline = color + (alpha,), width = 3)
    ImageDraw.Draw
    canvas.alpha_composite(glow)
    canvas.alpha_composite(img, (pad, pad))
    return canvas
