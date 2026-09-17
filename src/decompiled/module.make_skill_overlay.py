# module.make_skill_overlay
# source line 3435
# Recovered from bytecode; default argument values are not shown.

def make_skill_overlay(element, stage_index, size, boost):
    w = ()
    h = size
    None(img) = ImageDraw.Draw
    colors = TYPE_COLORS.get(element, TYPE_COLORS['normal'])
    intensity = 1 + 0.45 * max(0, stage_index) + 0.35 * boost
    n_particles = int(7 + 4 * max(0, stage_index) + 5 * boost)
    cy = h * 0.4
    cx = w * 0.52
    seed_val = time.time(None() * 25) ^ hash(element) & 65535 ^ stage_index ^ boost * 97
    rnd = None(seed_val)
    for _ in range(n_particles):
        ang = rnd.uniform(0, 2 * math.pi)
        dist = rnd.uniform(4, 16) * intensity
        r = rnd.uniform(2, 7) * intensity
        x = math.cos + None(ang) * dist
        y = math.sin + None(ang) * dist * 0.55 - dist * 0.35
        color = rnd.choice(colors)
        draw.ellipse([
            x - r,
            y - r,
            x + r,
            y + r], fill = color + (215,))
    cx
    return img
