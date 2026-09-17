# module.PetApp._build_combat_full._side_info
# source line 10858
# Recovered from bytecode; default argument values are not shown.

def _side_info(side):
    if side == 'wild':
        idle_act = entry.get('idle', 'Idle')
        th = None(ctx['wild_aset'], idle_act, spriteanim.DIR_LEFT, 1.5, 80)
        return (wild_img_label, ctx['wild_aset'], entry, spriteanim.DIR_LEFT, (lambda im: add_level_glow(im, wild_level)), th, render_wild)
    if None == 'body2':
        if has_body2 or ctx.get('body2_aset') is None:
            return None
        b2e = None['body2_entry']
        th = None(ctx['body2_aset'], b2e.get('idle', 'Idle'), spriteanim.DIR_RIGHT, 1.1, 60)
        return (body2_img_label, ctx['body2_aset'], b2e, spriteanim.DIR_RIGHT, None, th, render_body2)
    scale = None.body_display_scale() * 0.85
    aset = self.active_anim_set()
    th = None(aset, 'Idle', spriteanim.DIR_RIGHT, scale, 70)
    return (player_img_label, aset, player_entry, spriteanim.DIR_RIGHT, None, th, render_player)
