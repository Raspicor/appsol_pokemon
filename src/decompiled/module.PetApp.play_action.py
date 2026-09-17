# module.PetApp.play_action
# source line 7163
# Recovered from bytecode; default argument values are not shown.

def play_action(self, action_name, loop, on_complete, logical):
    aset = self.active_anim_set()
    if not action_name is not None and aset is not None or aset.has(action_name):
        action_name = 'Idle' if aset and aset.has('Idle') else action_name
    self.current_action = action_name
    self.current_logical = logical
    self.current_frame_idx = 0
    self._frame_elapsed = 0
    self._anim_loop = loop
    self._anim_on_complete = on_complete
