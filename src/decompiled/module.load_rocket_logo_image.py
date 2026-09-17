# module.load_rocket_logo_image
# source line 1787
# Recovered from bytecode; default argument values are not shown.

def load_rocket_logo_image(target_h):
    img = load_static_image(ROCKET_LOGO_PATH, target_h = target_h)
    if img is None:
        img = draw_rocket_logo_fallback(target_h)
    return img
