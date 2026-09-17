# module.PetApp.open_evolution_tab._icon_for
# source line 8433
# Recovered from bytecode; default argument values are not shown.

def _icon_for(dd, colored):
    entry = POKEDEX.get(dd)
    if not entry:
        return draw_pokeball_image(48)

    try:
        aset = None(sprite_folder_path(entry['en']))
        frame = aset.frame(entry['idle'], 0, spriteanim.DIR_DOWN)
        if frame is None:
            return draw_pokeball_image(48)
        frame = spriteanim.AnimSet.convert('RGBA')
        if not colored:
            frame = make_silhouette(frame)
        return frame
    except Exception:
        frame = None
        continue
