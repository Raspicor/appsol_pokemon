# module.PetApp._build_combat_full.render_wild
# source line 10679
# Recovered from bytecode; default argument values are not shown.

def render_wild(effect, crit):
    if ctx['wild_aset'] is None:
        ph = draw_pokeball_image(80)
        tkimg = None(ph)
        wild_img_label.image = tkimg
        wild_img_label.configure(image = tkimg)
        return None
    frame = None['wild_aset'].frame(entry['idle'], 0, spriteanim.DIR_LEFT)
    if frame is None:
        frame = ctx['wild_aset'].frame(entry['idle'], 0, spriteanim.DIR_DOWN)
    if frame is None:
        ph = draw_pokeball_image(80)
        tkimg = None(ph)
        wild_img_label.image = tkimg
        wild_img_label.configure(image = tkimg)
        return None
    frame = None.convert('RGBA')
    if effect:
    
        try:
            ov = make_skill_overlay(entry.get('element', 'normal'), 1, frame.size, boost = 2 if crit else 0)
            frame = None(frame, ov)
            frame = add_level_glow(frame, wild_level)
            _combat_scale = 1.5 * sprite_extra_scale(entry.get('dex'))
            frame = frame.resize((max(8, int(frame.width * _combat_scale)), max(8, int(frame.height * _combat_scale))), Image.NEAREST)
            tkimg = None(frame)
            wild_img_label.image = tkimg
            wild_img_label.configure(image = tkimg)
            return None
        except Exception:
            continue
