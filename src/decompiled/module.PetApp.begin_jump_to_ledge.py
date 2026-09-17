# module.PetApp.begin_jump_to_ledge
# source line 11610
# Recovered from bytecode; default argument values are not shown.

def begin_jump_to_ledge(self, ledge):
    target_x = (ledge['left'] + ledge['right']) // 2

    def _arrive():
        self._start_jump_visual(ledge)

    self.start_targeted_walk(target_x, _arrive)
