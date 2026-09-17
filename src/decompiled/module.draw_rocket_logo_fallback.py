# module.draw_rocket_logo_fallback
# source line 1765
# Recovered from bytecode; default argument values are not shown.

def draw_rocket_logo_fallback(size):
    img = None('RGBA', (size, size), (17, 17, 17, 255))
    draw = None(img)
    pad = max(1, size // 16)
    draw.ellipse([
        pad,
        pad,
        size - pad - 1,
        size - pad - 1], fill = (214, 30, 30, 255), outline = (0, 0, 0, 255), width = max(1, size // 20))

    try:
        font = None()
        if font is not None:
        
            try:
                bbox = draw.textbbox((0, 0), 'R', font = font)
                th = bbox[3] - bbox[1]
                tw = bbox[2] - bbox[0]
                draw.text(((size - tw) / 2 - bbox[0], (size - th) / 2 - bbox[1]), 'R', fill = (255, 255, 255, 255), font = font)
                return img
                return img
                except Exception:
                    ImageDraw.Draw
                    font = None
                    continue
            except Exception:
                ImageDraw.Draw
                return img
