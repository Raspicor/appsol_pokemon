# module.MiniPreview._compose
# source line 3975
# Recovered from bytecode; default argument values are not shown.

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
