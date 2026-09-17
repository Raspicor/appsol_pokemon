# module.PetApp.redraw
# source line 7223
# Recovered from bytecode; default argument values are not shown.

def redraw(self):
    frame = self._current_frame_image()
    if frame is None:
        return None
    if None._fx_kind:
        elapsed = None() - self._fx_started_at
        if elapsed < self._fx_duration:
            progress = elapsed / self._fx_duration if self._fx_duration > 0 else 1
        
            try:
                fx_overlay = make_levelup_fx_overlay(self._fx_kind, frame.size, progress)
                frame = None(frame, fx_overlay)
            self._fx_kind = None
            scale = self.body_display_scale() * self.state.get('manual_scale', 1) * self._weight_factor() * sprite_extra_scale(self.player_dex())
            w = max(8, int(frame.width * scale))
            h = max(8, int(frame.height * scale))
            try:
                resized = frame.resize((w, h), Image.NEAREST)
                alpha = resized.split()[3]
                alpha = alpha.point((lambda a: if a >= 128:
    255))
                resized.putalpha(alpha)
                bg = None('RGB', (w, h), (255, 0, 255))
                bg.paste(resized, (0, 0), resized)
                self._tkimg = None(bg)
                self.label.configure(image = self._tkimg)
                self._img_w, self._img_h = w, h
                if self.behavior_state == 'held':
                    return None
                left = ImageTk.PhotoImage(self.pos_x - w / 2)
                top = int(self.pos_y - h)
                left = max(self.screen_left, min(self.screen_left + self.screen_w - w, left))
                top = max(self.screen_top, min(self.screen_top + self.screen_h - h, top))
            
                try:
                    self.root.geometry(f'''{w}x{h}+{left}+{top}''')
                    return None
                    except Exception:
                        Image.alpha_composite
                        continue
                    except Exception:
                        Image.alpha_composite
                        return None
                except Exception:
                    Image.alpha_composite
                    return None
