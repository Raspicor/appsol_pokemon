# module.PetApp.open_game_memory._finish
# source line 6095
# Recovered from bytecode; default argument values are not shown.

def _finish():
    mistakes = ctx['mistakes']
    if mistakes <= 1:
        tier = 'gold'
    elif mistakes <= 3:
        tier = 'silver'
    elif mistakes <= 5:
        tier = 'bronze'
    else:
        tier = 'fail'
    result_lines = [
        f'''클리어! 실수 {mistakes}회''',
        self._minigame_tier_label(tier)]
    if practice:
        self._show_minigame_result_popup(win, True, result_lines + [
            '(연습이라 보상은 없어요)'], close_fn = _on_close, retry_fn = (lambda : self.open_game_memory(practice = True)))
        return None
    msgs = None._minigame_claim('card', tier)
    self._refresh_minigame_hub()
    self._show_minigame_result_popup(win, False, result_lines + msgs, close_fn = _on_close)
