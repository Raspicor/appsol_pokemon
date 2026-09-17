# module.PetApp.active_anim_set
# source line 6924
# Recovered from bytecode; default argument values are not shown.

def active_anim_set(self):
    mid = self._mega_sprite_id()
    if mid:
        aset = self._mega_anim_sets.get(mid)
        if aset is None:
        
            try:
                aset = None(sprite_folder_path(mid))
                self._mega_anim_sets[mid] = aset
                if aset is not None:
                    return aset
                return spriteanim.AnimSet.anim_sets.get(self.stage_conf()['id'])
            except Exception:
                aset = None
                continue
