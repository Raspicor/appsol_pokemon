# module.PetApp._tray_image
# source line 17552
# Recovered from bytecode; default argument values are not shown.

def _tray_image(self):
    try:
        aset = self.active_anim_set()
        if aset:
        
            try:
                pass
            frame = None
            if frame is None:
                return None('RGBA', (32, 32), (255, 255, 255, 255))
            return aset.frame('Idle', 0, spriteanim.DIR_DOWN).convert('RGBA').resize((32, 32), Image.NEAREST)
            except Exception:
                return 
