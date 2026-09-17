# module.PetApp._build_compact_battle.render
# source line 10222
# Recovered from bytecode; default argument values are not shown.

def render(effect_side, crit):
    if ctx['wild_aset'] is not None:
        frame = ctx['wild_aset'].frame(ctx['entry']['idle'], 0, spriteanim.DIR_DOWN)
        if frame is not None:
            frame = frame.convert('RGBA')
            if effect_side == 'wild':
            
                try:
                    ov = make_skill_overlay(ctx['entry'].get('element', 'normal'), 1, frame.size, boost = 2 if crit else 0)
                    frame = None(frame, ov)
                    frame = add_level_glow(frame, ctx['wild_level'])
                    s = WILD_TARGET_H / max(1, frame.height)
                    frame = frame.resize((max(8, int(frame.width * s)), max(8, int(frame.height * s))), Image.NEAREST)
                    tkimg = None(frame)
                    wild_img_label.image = tkimg
                    wild_img_label.configure(image = tkimg)
                ph = draw_pokeball_image(WILD_TARGET_H)
                tkimg = None(ph)
                wild_img_label.image = tkimg
                except:
                    ph = draw_pokeball_image(WILD_TARGET_H)
                    tkimg = None(ph)
                    wild_img_label.image = tkimg
                    wild_img_label.configure(image = tkimg)

                aset = self.active_anim_set()
                if aset is not None:
                    frame = aset.frame('Idle', 0, spriteanim.DIR_RIGHT)
                    if frame is not None:
                        frame = frame.convert('RGBA')
                        if effect_side == 'player':
                        
                            try:
                                ov = make_skill_overlay(self.current_element(), self.state.get('stage', 0), frame.size, boost = 2 if crit else 0)
                                frame = None(frame, ov)
                                if body_hp(ctx, 'player') <= 0:
                                    frame.putalpha(90)
                                s = PLAYER_TARGET_H / max(1, frame.height)
                                frame = frame.resize((max(8, int(frame.width * s)), max(8, int(frame.height * s))), Image.NEAREST)
                                tkimg = None(frame)
                                player_img_label.image = tkimg
                                player_img_label.configure(image = tkimg)
                                if has_body2:
                                    if ctx.get('body2_aset') is not None:
                                        frame = ctx['body2_aset'].frame(ctx['body2_entry'].get('idle', 'Idle'), 0, spriteanim.DIR_RIGHT)
                                        if frame is not None:
                                            frame = frame.convert('RGBA')
                                            if effect_side == 'body2':
                                            
                                                try:
                                                    ov = make_skill_overlay(ctx['body2_entry'].get('element', 'normal'), 1, frame.size, boost = 2 if crit else 0)
                                                    frame = None(frame, ov)
                                                    if body_hp(ctx, 'body2') <= 0:
                                                        frame.putalpha(90)
                                                    s = PLAYER_TARGET_H / max(1, frame.height)
                                                    frame = frame.resize((max(8, int(frame.width * s)), max(8, int(frame.height * s))), Image.NEAREST)
                                                    tkimg = None(frame)
                                                    body2_img_label.image = tkimg
                                                    body2_img_label.configure(image = tkimg)
                                                    return None
                                                    return None
                                                    return None
                                                    return None
                                                    except Exception:
                                                        Image.alpha_composite
                                                        continue
                                                    except Exception:
                                                        Image.alpha_composite
                                                        continue
                                                except Exception:
                                                    Image.alpha_composite
                                                    continue
