# module.PetApp.open_game_omok
# source line 6568
# Recovered from bytecode; default argument values are not shown.

def open_game_omok(self):
    if self._minigame_window_active():
        None('PikaPet', '이미 다른 미니게임 창이 열려 있어요! 먼저 그 창을 닫아주세요.')
        return None
    None._omok_mode_dialog()
