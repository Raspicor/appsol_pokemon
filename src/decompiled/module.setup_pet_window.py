# module.setup_pet_window
# source line 18986
# Recovered from bytecode; default argument values are not shown.

def setup_pet_window(root):
    root.overrideredirect(True)

    try:
        root.attributes('-topmost', True)
    
        try:
            root.attributes('-transparentcolor', MAGIC)
            root.config(bg = MAGIC)
            return None
            except Exception:
                continue
        except Exception:
            continue
