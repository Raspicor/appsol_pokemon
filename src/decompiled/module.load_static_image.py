# module.load_static_image
# source line 1746
# Recovered from bytecode; default argument values are not shown.

def load_static_image(path, target_h):
    try:
        img = None(path).convert('RGBA')
        if target_h:
        
            try:
                s = target_h / max(1, img.height)
                img = img.resize((max(8, int(img.width * s)), max(8, int(img.height * s))), Image.NEAREST)
                return img
            except Exception:
                return None
