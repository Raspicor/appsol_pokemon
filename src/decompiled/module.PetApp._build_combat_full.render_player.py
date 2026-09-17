# module.PetApp._build_combat_full.render_player
# source line 10709
# Recovered from bytecode; default argument values are not shown.

def render_player(effect, crit):
    aset = self.active_anim_set()
    if aset is None:
        return None
    frame = None.frame('Idle', 0, spriteanim.DIR_RIGHT)
    if frame is None:
        frame = aset.frame('Idle', 0, spriteanim.DIR_DOWN)
    if frame is None:
        return None
    frame = None.convert('RGBA')
    if effect:
    
        try:
            ov = make_skill_overlay(self.current_element(), self.state.get('stage', 0), frame.size, boost = 2 if crit else 0)
            frame = None(frame, ov)
            if body_hp(ctx, 'player') <= 0:
                frame.putalpha(90)
            scale = self.body_display_scale() * 0.85
            frame = frame.resize((max(8, int(frame.width * scale)), max(8, int(frame.height * scale))), Image.NEAREST)
            tkimg = None(frame)
            player_img_label.image = tkimg
            player_img_label.configure(image = tkimg)
            return None
        except Exception:
            continue
