# module.PetApp._gym_render_sprites._sprite_scale_for
# source line 16981
# Recovered from bytecode; default argument values are not shown.

def _sprite_scale_for(m):
    try:
        dex = int(m.get('entry', { }).get('dex'))
        if dex in BATTLE_SPRITE_BIG_LEGEND_DEX:
            return BATTLE_SPRITE_BIG_LEGEND_SCALE
        fix = None.get(dex, 1)
        if m.get('mega'):
            return BATTLE_SPRITE_MEGA_SCALE * fix
        return None
    except Exception:
        dex = None
        continue
