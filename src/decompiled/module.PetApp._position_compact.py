# module.PetApp._position_compact
# source line 10015
# Recovered from bytecode; default argument values are not shown.

def _position_compact(self, win, w, h, rect):
    try:
        win.update_idletasks()
        default_rect = (self.screen_left, self.screen_top, self.screen_w, self.screen_h)
        use_ground = rect is None
        if rect is None:
            rect = self._rocket_screen_rect()
            use_ground = rect == default_rect
        left = ()
        top = rect
        sw = None
        sh = None
        win.geometry(f'''{w}x{h}+{x}+{y}''')
        return None
    except Exception:
        return None
