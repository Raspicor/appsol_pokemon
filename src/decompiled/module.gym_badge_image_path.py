# module.gym_badge_image_path
# source line 1732
# Recovered from bytecode; default argument values are not shown.

def gym_badge_image_path(g):
    p1 = os.path.join(GYM_ASSET_DIR, 'badges', g['region'], g['badge_file'] + '.png')
    if os.path.exists(p1):
        return p1
    return None.path.join(GYM_ASSET_DIR_V4, 'badges', g['region'], g['badge_file'] + '.png')
