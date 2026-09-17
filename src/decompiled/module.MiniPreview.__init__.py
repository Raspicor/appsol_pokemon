# module.MiniPreview.__init__
# source line 3963
# Recovered from bytecode; default argument values are not shown.

def __init__(self, parent, anim_set, size, idle_name, **kw):
    bg = kw.pop('bg', '#f4f4f4')
    super().__init__(parent, bg = bg, bd = 0)
    self.anim_set = anim_set
    self.size = size
    self.idle_name = idle_name
    self.frame_idx = 0
    self.ball_img = draw_pokeball_image(size)
    self._tk = None
    self._running = True
    self._animate()
