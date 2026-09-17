# module.add_mega_aura
# source line 3640
# Recovered from bytecode; default argument values are not shown.

def add_mega_aura(img, intensity):
    if intensity <= 0.001:
        return img
    img = None.convert('RGBA')
    pad = 11
    w = ()
    h = img.size
    None('RGBA', canvas.size, (0, 0, 0, 0)) = Image.new
    gd = None(glow)
    t = None()
    rings = 4
    for i in range(rings):
        rr = pad - i * 1.7
        if rr <= 0:
            continue
        hue = (t * 0.12 + i * 0.16) % 1
        rf = ()
        gf = None(hue, 0.65, 1)
        int(max(8, 95 - i * 18) * intensity) = (int(rf * 255), int(gf * 255), int(bf * 255), color)
        gd.ellipse([
            pad - rr,
            pad - rr,
            w + pad + rr,
            h + pad + rr], outline = color + (alpha,), width = 3)
    range(rings)
    canvas.alpha_composite(glow)
    canvas.alpha_composite(img, (pad, pad))
    return canvas
