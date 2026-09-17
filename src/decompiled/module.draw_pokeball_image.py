# module.draw_pokeball_image
# source line 3478
# Recovered from bytecode; default argument values are not shown.

def draw_pokeball_image(size):
    img = None('RGBA', (size, size), (0, 0, 0, 0))
    d = None(img)
    r = size // 2 - 4
    cx = size // 2
    cy = size // 2
    d.pieslice([
        cx - r,
        cy - r,
        cx + r,
        cy + r], 180, 360, fill = (226, 60, 60, 255))
    d.pieslice([
        cx - r,
        cy - r,
        cx + r,
        cy + r], 0, 180, fill = (250, 250, 250, 255))
    d.ellipse([
        cx - r,
        cy - r,
        cx + r,
        cy + r], outline = (25, 25, 25, 255), width = max(2, size // 35))
    band_h = max(4, size // 14)
    d.rectangle([
        cx - r,
        cy - band_h // 2,
        cx + r,
        cy + band_h // 2], fill = (25, 25, 25, 255))
    br = max(8, size // 7)
    d.ellipse([
        cx - br,
        cy - br,
        cx + br,
        cy + br], fill = (250, 250, 250, 255), outline = (25, 25, 25, 255), width = max(2, size // 40))
    br2 = int(br * 0.5)
    d.ellipse([
        cx - br2,
        cy - br2,
        cx + br2,
        cy + br2], outline = (25, 25, 25, 255), width = max(1, size // 60))
    return img
