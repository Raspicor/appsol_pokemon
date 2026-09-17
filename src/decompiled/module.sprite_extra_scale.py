# module.sprite_extra_scale
# source line 477
# Recovered from bytecode; default argument values are not shown.

def sprite_extra_scale(dex):
    try:
        dex = int(dex)
        if dex in BATTLE_SPRITE_BIG_LEGEND_DEX:
            return BATTLE_SPRITE_BIG_LEGEND_SCALE
        return None.get(dex, 1)
    except Exception:
        return 1
