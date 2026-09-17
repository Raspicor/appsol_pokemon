# module.draw_completion_badge
# source line 3504
# Recovered from bytecode; default argument values are not shown.

def draw_completion_badge(size, gen):
    color = GEN_BADGE_COLORS.get(gen, (255, 215, 0))
    dark = (lambda .0: for c in .0:
    max(0, c - 70).0) if tuple is <common_constant> else (lambda .0: for c in .0:
    max(0, c - 70).0)(color())
    h = int(size * 1.35)
    img = None('RGBA', (size, h), (0, 0, 0, 0))
    d = None(img)
    cx = size // 2
    cy = size // 2
    r = size // 2 - 6
    tail_w = max(6, size // 6)
    d.polygon([
        (cx - tail_w, cy + r - 6),
        (cx - tail_w // 2, h - 2),
        (cx, cy + r + size // 5),
        (cx + tail_w // 2, h - 2),
        (cx + tail_w, cy + r - 6)], fill = dark)
    d.ellipse([
        cx - r,
        cy - r,
        cx + r,
        cy + r], fill = color + (255,), outline = (50, 35, 10, 255), width = max(2, size // 45))
    d.ellipse([
        (cx - r) + 8,
        (cy - r) + 8,
        cx + r - 8,
        cy + r - 8], outline = (255, 255, 255, 110), width = 2)
    star_r_out = r * 0.55
    star_r_in = star_r_out * 0.42
    pts = []
    for i in range(10):
        ang = -(math.pi) / 2 + i * math.pi / 5
        rr = star_r_out if i % 2 == 0 else star_r_in
        rr + math.cos * None(ang)((cy, rr + math.sin * None(ang)))
    pts.append
    d.polygon(pts, fill = (255, 255, 255, 235))
    return img
