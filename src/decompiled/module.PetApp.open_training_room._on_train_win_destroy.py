# module.PetApp.open_training_room._on_train_win_destroy
# source line 15507
# Recovered from bytecode; default argument values are not shown.

def _on_train_win_destroy(_e):
    if getattr(self, '_active_training_win', None) is win:
        self._active_training_win = None
        return None
