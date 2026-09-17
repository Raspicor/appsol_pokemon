# module.MiniPreview
# source line 3962
# Recovered from bytecode; default argument values are not shown.

def MiniPreview():
    __firstlineno__ = 3962
    __classdict__ = <NODE:36>

    def __init__(self, parent, anim_set, size = 110, idle_name = 'Idle', **kw):
        '''bg'''
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


    def _compose(self):
        base = self.ball_img.copy()
        frame = None
    
        try:
            frame = self.anim_set.frame(self.idle_name, self.frame_idx, spriteanim.DIR_DOWN)
            if frame is not None:
            
                try:
                    target_h = int(self.size * 0.62)
                    scale = target_h / max(1, frame.height)
                    target_w = max(1, int(frame.width * scale))
                    char = frame.convert('RGBA').resize((target_w, target_h), Image.NEAREST)
                    px = (self.size - target_w) // 2
                    py = int(self.size * 0.5 - target_h * 0.68)
                    base.alpha_composite(char, (px, py))
                    self._tk = None(base)
                    self.configure(image = self._tk)
                    return None
                    except Exception:
                        frame = None
                        continue
                except Exception:
                    continue




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




    def stop(self):
        self._running = False

    __static_attributes__ = ('_running', '_tk', 'anim_set', 'ball_img', 'frame_idx', 'idle_name', 'size')
    __classdictcell__ = __classdict__
    __classcell__ = __class__
    return __class__
