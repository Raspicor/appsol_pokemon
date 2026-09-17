# module.PetApp._ensure_body_anim_loaded
# source line 4752
# Recovered from bytecode; default argument values are not shown.

def _ensure_body_anim_loaded(self, dex):
    key = f'''pdx_{dex}'''
    if key in self.anim_sets:
        return None
    entry = None.get(int(dex))
    if not entry:
        return None

    try:
        self.anim_sets[key] = None(sprite_folder_path(entry['en']))
        return None
    except Exception:
        return None
