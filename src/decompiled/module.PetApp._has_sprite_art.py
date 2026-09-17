# module.PetApp._has_sprite_art
# source line 13698
# Recovered from bytecode; default argument values are not shown.

def _has_sprite_art(self, entry):
    try:
        return os.path.isdir(sprite_folder_path(entry.get('en', '')))
    except Exception:
        return False
