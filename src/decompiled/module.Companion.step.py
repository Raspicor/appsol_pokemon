# module.Companion.step
# source line 4220
# Recovered from bytecode; default argument values are not shown.

def step(self, dt_ms):
    if not self.anim_set or self.entry:
        return None
    layout = None.owner.state.get('companion_layout', 'line')
    if layout == 'free':
        if not self._dragging:
            self._step_free_roam(dt_ms)
        direction = self.direction if self.direction is not None else self.owner.direction
    elif self._synced_sleep and self.anim_set.has('Sleep'):
        self.action = 'Sleep'
    elif self.action == 'Sleep':
        self.action = self.entry['idle']
        self.frame_idx = 0
    direction = self.owner.direction
    self.anim_set.duration_of(self.action, self.frame_idx) * ANIM_TICK_MS = self, self._elapsed += dt_ms, ._elapsed
    if dur <= 0:
        dur = ANIM_TICK_MS
    if self._elapsed >= dur:
        self.anim_set.n_frames(self.action) = self, self._elapsed -= dur, ._elapsed
        if n > 0:
            self.frame_idx = (self.frame_idx + 1) % n
    frame = self.anim_set.frame(self.action, self.frame_idx, direction)
    if frame is None:
        return None
    scale = None(self.entry) * self.owner.state.get('manual_scale', 1) * sprite_extra_scale(self.dex)
    w = max(8, int(frame.width * scale))
    h = max(8, int(frame.height * scale))

    try:
        resized = frame.convert('RGBA').resize((w, h), Image.NEAREST)
        alpha = resized.split()[3]
        alpha = alpha.point((lambda a: if a >= 128:
    255))
        resized.putalpha(alpha)
        bg = None('RGB', (w, h), (255, 0, 255))
        bg.paste(resized, (0, 0), resized)
        self._tkimg = None(bg)
        self.label.configure(image = self._tkimg)
        self._img_w, self._img_h = w, h
        if self._dragging:
        
            try:
                self.win.geometry(f'''{w}x{h}''')
                return None
            
                try:
                    self.win.geometry(f'''{w}x{h}+{left}+{top}''')
                    if not self._first_positioned:
                    
                        try:
                            self.win.deiconify()
                            self._first_positioned = True
                            return None
                            return None
                            except Exception:
                                Image.new
                                return None
                            except Exception:
                                Image.new
                                return None
                        except Exception:
                            Image.new
                            return None
