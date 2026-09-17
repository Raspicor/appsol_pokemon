# module.load_infinite_stone_image
# source line 1822
# Recovered from bytecode; default argument values are not shown.

def load_infinite_stone_image(broken, target_h, grayscale):
    path = INFINITE_STONE_BROKEN_PATH if broken else INFINITE_STONE_BIG_PATH
    img = load_static_image(path, target_h = target_h)
    if img is None:
        img = draw_infinite_stone_fallback(target_h, broken)
    if grayscale:
        img = _to_grayscale_keep_alpha(img)
    return img
