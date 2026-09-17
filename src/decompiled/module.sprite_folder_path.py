# module.sprite_folder_path
# source line 108
# Recovered from bytecode; default argument values are not shown.

def sprite_folder_path(name):
    for base in SPRITE_SEARCH_DIRS:
        p = os.path.join(base, name)
        if not os.path.isdir(p):
            continue
    
        return SPRITE_SEARCH_DIRS, p
    return os.path.join(SPRITE_DIR, name)
