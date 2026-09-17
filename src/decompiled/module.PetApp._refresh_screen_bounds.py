# module.PetApp._refresh_screen_bounds
# source line 5016
# Recovered from bytecode; default argument values are not shown.

def _refresh_screen_bounds(self, force):
    left = ()
    top = self._compute_screen_rect()
    w = None
    h = None
    if w <= 0 or h <= 0:
        return None
    if not None and left != self.screen_left:
        left != self.screen_left
        if not top != self.screen_top:
            top != self.screen_top
            if not w != self.screen_w:
                w != self.screen_w
    (self.screen_left, self.screen_top, self.screen_w, self.screen_h) = (left, top, w, h)

    try:
        self.taskbar_rect = None()
        if changed:
            self._clamp_to_screen()
            return None
        return winlayer.get_taskbar_rect
    except Exception:
        continue
