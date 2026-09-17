# module.PetApp._current_frame_image
# source line 7205
# Recovered from bytecode; default argument values are not shown.

def _current_frame_image(self):
    aset = self.active_anim_set()
    if aset is None:
        return None
    frame = None.frame(self.current_action, self.current_frame_idx, self.direction)
    if frame is None:
        frame = aset.frame('Idle', 0, self.direction)
    if frame is None:
        return None
    frame = None.convert('RGBA')
    if self.current_logical == 'skill':
    
        try:
            overlay = make_skill_overlay(self.current_element(), self.state.get('stage', 0), frame.size)
            frame = None(frame, overlay)
            return frame
            return frame
        except Exception:
            return frame
