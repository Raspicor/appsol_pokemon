# module._to_grayscale_keep_alpha
# source line 1832
# Recovered from bytecode; default argument values are not shown.

def _to_grayscale_keep_alpha(img):
    try:
        img = img.convert('RGBA')
        alpha = img.getchannel('A')
        gray = img.convert('L').convert('RGBA')
        gray.putalpha(alpha)
        return gray
    except Exception:
        return 
