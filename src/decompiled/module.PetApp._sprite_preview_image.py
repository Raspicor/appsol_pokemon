# module.PetApp._sprite_preview_image
# source line 13667
# Recovered from bytecode; default argument values are not shown.

def _sprite_preview_image(self, dex, size, level, silhouette):
    entry = POKEDEX.get(dex) if dex is not None else None
    frame = None
    if entry:
    
        try:
            aset = None(sprite_folder_path(entry['en']))
            frame = aset.frame(entry.get('idle', 'Idle'), 0, spriteanim.DIR_DOWN)
            frame = frame.convert('RGBA')
            if silhouette:
                frame = make_silhouette(frame)
            else:
            
                try:
                    if level:
                    
                        try:
                            frame = add_level_glow(frame, level)
                            if frame is None:
                                frame = None('RGBA', (48, 48), (0, 0, 0, 0))
                                d = None(frame)
                            
                                try:
                                    d.rounded_rectangle([
                                        2,
                                        2,
                                        45,
                                        45], radius = 8, fill = (210, 210, 210, 255), outline = (150, 150, 150, 255), width = 2)
                                    d.text((18, 14), '?', fill = (90, 90, 90, 255))
                                    scale = max(1, size / max(frame.width, frame.height))
                                    frame = frame.resize((max(8, int(frame.width * scale)), max(8, int(frame.height * scale))), Image.NEAREST)
                                    return None(frame)
                                    except Exception:
                                        ImageDraw.Draw
                                        frame = None
                                        continue
                                except Exception:
                                    Image.new
                                    d.rectangle([
                                        2,
                                        2,
                                        45,
                                        45], fill = (210, 210, 210, 255), outline = (150, 150, 150, 255), width = 2)
                                    continue
