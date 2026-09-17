# module.PetApp._build_combat_full.render_body2
# source line 10734
# Recovered from bytecode; default argument values are not shown.

def render_body2(effect, crit):
    if has_body2 or ctx.get('body2_aset') is None:
        return None
    b2e = None['body2_entry']
    frame = ctx['body2_aset'].frame(b2e.get('idle', 'Idle'), 0, spriteanim.DIR_RIGHT)
    if frame is None:
        return None
    frame = None.convert('RGBA')
    if effect:
    
        try:
            ov = make_skill_overlay(b2e.get('element', 'normal'), 1, frame.size, boost = 2 if crit else 0)
            frame = None(frame, ov)
            if body_hp(ctx, 'body2') <= 0:
                frame.putalpha(90)
            frame = frame.resize((max(8, int(frame.width * 1.1)), max(8, int(frame.height * 1.1))), Image.NEAREST)
            tkimg = None(frame)
            body2_img_label.image = tkimg
            body2_img_label.configure(image = tkimg)
            return None
        except Exception:
            continue
