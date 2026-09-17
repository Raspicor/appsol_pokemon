# module.PetApp.open_infinite_stone._shake
# source line 5839
# Recovered from bytecode; default argument values are not shown.

def _shake(step):
    offsets = [
        -6,
        6,
        -4,
        4,
        -2,
        0]
    if step >= len(offsets):
        return None

    try:
        img_label.place(relx = 0.5, rely = 0.5, anchor = 'center', x = offsets[step])
        win.after(35, (lambda : None(step + 1)))
        return None
    except Exception:
        return None
