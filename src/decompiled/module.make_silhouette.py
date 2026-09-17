# module.make_silhouette
# source line 3534
# Recovered from bytecode; default argument values are not shown.

def make_silhouette(img):
    img = img.convert('RGBA')
    alpha = img.split()[3]
    black = None('RGBA', img.size, (20, 20, 24, 255))
    black.putalpha(alpha)
    return black
