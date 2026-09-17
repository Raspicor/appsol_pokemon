# module.PetApp.advance_animation
# source line 7174
# Recovered from bytecode; default argument values are not shown.

def advance_animation(self, dt_ms):
    aset = self.active_anim_set()
    if aset is None:
        return None
    0 = None, None._frame_elapsed += dt_ms, ._frame_elapsed
    if guard < 50:
        guard += 1
        dur = aset.duration_of(self.current_action, self.current_frame_idx) * ANIM_TICK_MS
        if dur <= 0:
            dur = ANIM_TICK_MS
        if self._frame_elapsed < dur:
            return None
        aset.n_frames(self.current_action) = None, None._frame_elapsed -= dur, ._frame_elapsed
        if n <= 0:
            return None
        nxt = None.current_frame_idx + 1
        if nxt >= n:
            if self._anim_loop:
                self.current_frame_idx = 0
                continue
            self.current_frame_idx = n - 1
            cb = self._anim_on_complete
            self._anim_on_complete = None
            if cb:
                None()
            return None
        None.current_frame_idx = None
        continue
