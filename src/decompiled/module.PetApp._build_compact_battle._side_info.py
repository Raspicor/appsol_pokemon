# module.PetApp._build_compact_battle._side_info
# source line 10315
# Recovered from bytecode; default argument values are not shown.

def _side_info(side):
    if side == 'wild':
        return (wild_img_label, ctx['wild_aset'], ctx['entry'], spriteanim.DIR_DOWN, (lambda im: add_level_glow(im, ctx['wild_level'])), WILD_TARGET_H)
    if None == 'body2':
        if not has_body2:
            return None
        return (None, ctx.get('body2_aset'), ctx.get('body2_entry', { }), spriteanim.DIR_RIGHT, None, PLAYER_TARGET_H)
    return (None, self.active_anim_set(), ctx['player_entry'], spriteanim.DIR_RIGHT, None, PLAYER_TARGET_H)
