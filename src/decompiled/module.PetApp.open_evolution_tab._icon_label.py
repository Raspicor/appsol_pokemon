# module.PetApp.open_evolution_tab._icon_label
# source line 8449
# Recovered from bytecode; default argument values are not shown.

def _icon_label(parent, dd, colored, target_h, highlight):
    cell = None(parent, relief = 'solid' if highlight else 'flat', bd = 2 if highlight else 0, padx = 2, pady = 2)
    img = None(dd, colored)
    s = target_h / max(1, img.height)
    img = img.resize((max(8, int(img.width * s)), max(8, int(img.height * s))), Image.NEAREST)
    tkimg = None(img)
    lbl = None(cell, image = tkimg)
    lbl.image = tkimg
    lbl.pack()
    return cell
