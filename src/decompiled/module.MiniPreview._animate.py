# module.MiniPreview._animate
# source line 3996
# Recovered from bytecode; default argument values are not shown.

def _animate(self):
    if not self._running:
        return None

    try:
        n = self.anim_set.n_frames(self.idle_name)
        if n > 0:
            self.frame_idx = (self.frame_idx + 1) % n
        self._compose()
    
        try:
            self.after(180, self._animate)
            return None
            except Exception:
                return None
        except Exception:
            return None
