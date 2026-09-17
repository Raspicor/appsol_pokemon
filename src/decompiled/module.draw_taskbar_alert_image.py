# module.draw_taskbar_alert_image
# source line 3457
# Recovered from bytecode; default argument values are not shown.

def draw_taskbar_alert_image(size):
    img = None('RGBA', (size, size), (0, 0, 0, 0))
    d = None(img)
    r = size // 2 - 2
    cx = size // 2
    cy = size // 2
    d.ellipse([
        cx - r,
        cy - r,
        cx + r,
        cy + r], fill = (255, 140, 0, 255), outline = (140, 70, 0, 255), width = max(1, size // 20))

    try:
        font = None('arialbd.ttf', int(size * 0.62))
        text = '!'
        bbox = d.textbbox((0, 0), text, font = font)
        th = bbox[3] - bbox[1]
        tw = bbox[2] - bbox[0]
        d.text((cx - tw / 2 - bbox[0], cy - th / 2 - bbox[1]), text, fill = (255, 255, 255, 255), font = font)
        return img
    except Exception:
        Image.new
        font = None()
        continue
