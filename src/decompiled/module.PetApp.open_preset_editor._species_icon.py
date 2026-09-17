# module.PetApp.open_preset_editor._species_icon
# source line 15296
# Recovered from bytecode; default argument values are not shown.

def _species_icon(dex, size):
    e = POKEDEX.get(dex, { })
    frame = None

    try:
        aset = None(sprite_folder_path(e.get('en')))
        frame = aset.frame(e.get('idle', 'Idle'), 0, spriteanim.DIR_DOWN)
        if frame is None:
            return draw_pokeball_image(size)
        frame = spriteanim.AnimSet.convert('RGBA')
        s = size / max(1, frame.height)
        return frame.resize((max(8, int(frame.width * s)), max(8, int(frame.height * s))), Image.NEAREST)
    except Exception:
        frame = None
        continue
