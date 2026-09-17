# module.gym_trainer_image_path
# source line 1739
# Recovered from bytecode; default argument values are not shown.

def gym_trainer_image_path(g):
    p1 = os.path.join(GYM_ASSET_DIR, 'trainers', g['region'], g['trainer_file'] + '.png')
    if os.path.exists(p1):
        return p1
    return None.path.join(GYM_ASSET_DIR_V4, 'sinnoh_leaders', g['trainer_file'] + '.png')
