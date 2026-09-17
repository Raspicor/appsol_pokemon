# module.make_levelup_fx_overlay
# source line 3668
# Recovered from bytecode; default argument values are not shown.

def make_levelup_fx_overlay(kind, size, progress):
    w = ()
    h = size
    max(0, 1 - progress) = None('RGBA', (w, h), (0, 0, 0, 0))
    if fade <= 0.01:
        return img
    draw = None(img)
    is_evolve = kind == 'evolve'
    cy = h * 0.42
    cx = w * 0.5
    t = None()
    n_particles = 22 if is_evolve else 14
    max_dist = max(w, h) * 0.62 * (0.35 + 0.75 * progress)
    for i in range(n_particles):
        ang = (i / n_particles) * 2 * math.pi + t * 2.2 if is_evolve else 1.4
        dist = max_dist * (0.55 + 0.45 * (i * 37 % 11) / 10)
        r = 3.2 if is_evolve else 2.6 * fade + 1
        x = math.cos + None(ang) * dist
        y = math.sin + None(ang) * dist * 0.8
        alpha = int(235 * fade)
        if alpha <= 0:
            continue
        draw.ellipse([
            x - r,
            y - r,
            x + r,
            y + r], fill = color + (alpha,))
    cy
    ring_r = min(w, h) * 0.5 * (0.5 + 0.5 * progress)
    ring_color = (255, 255, 255) if is_evolve else (255, 224, 120)
    ring_alpha = int(140 * fade)
    if ring_alpha > 0:
        draw.ellipse([
            cx - ring_r,
            cy - ring_r,
            cx + ring_r,
            cy + ring_r], outline = ring_color + (ring_alpha,), width = 3)
    return img
