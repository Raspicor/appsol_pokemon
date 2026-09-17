# module.PetApp._sprite_card_image
# source line 13707
# Recovered from bytecode; default argument values are not shown.

def _sprite_card_image(self, dex, size):
    entry = POKEDEX.get(dex) if dex is not None else None
    frame = None
    if entry:
    
        try:
            aset = None(sprite_folder_path(entry['en']))
            frame = aset.frame(entry.get('idle', 'Idle'), 0, spriteanim.DIR_DOWN)
            frame = frame.convert('RGBA')
            canvas_img = None('RGBA', (size, size), (0, 0, 0, 0))
            if frame is not None and frame.width > 0 and frame.height > 0:
                inner = size - 6
                scale = inner / max(frame.width, frame.height)
                new_w = max(8, int(frame.width * scale))
                new_h = max(8, int(frame.height * scale))
                frame = frame.resize((new_w, new_h), Image.NEAREST)
                ox = (size - new_w) // 2
                oy = (size - new_h) // 2
                canvas_img.paste(frame, (ox, oy), frame)
            else:
                d = None(canvas_img)
            
                try:
                    d.rounded_rectangle([
                        2,
                        2,
                        size - 3,
                        size - 3], radius = 8, fill = (210, 210, 210, 255), outline = (150, 150, 150, 255), width = 2)
                    d.text((size // 2 - 5, size // 2 - 8), '?', fill = (90, 90, 90, 255))
                    return None(canvas_img)
                    except Exception:
                        ImageDraw.Draw
                        frame = None
                        continue
                except Exception:
                    Image.new
                    d.rectangle([
                        2,
                        2,
                        size - 3,
                        size - 3], fill = (210, 210, 210, 255), outline = (150, 150, 150, 255), width = 2)
                    continue
