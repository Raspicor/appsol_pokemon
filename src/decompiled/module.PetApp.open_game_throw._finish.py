# module.PetApp.open_game_throw._finish
# source line 6457
# Recovered from bytecode; default argument values are not shown.

def _finish():
    None()
    hits = ctx['hits']
    if hits >= 5:
        tier = 'gold'
    elif hits >= 4:
        tier = 'silver'
    elif hits >= 2:
        tier = 'bronze'
    else:
        tier = 'fail'
    canvas.delete('all')
    canvas.create_text(150, 60, text = f'''결과: {hits}/{ctx['rounds']}개 성공''', font = ('맑은 고딕', 13, 'bold'))
    canvas.create_text(150, 90, text = self._minigame_tier_label(tier), font = ('맑은 고딕', 12))
    result_lines = [
        f'''결과: {hits}/{ctx['rounds']}개 성공''',
        self._minigame_tier_label(tier)]
    if practice:
        self._show_minigame_result_popup(win, True, result_lines + [
            '(연습이라 보상은 없어요)'], close_fn = _on_close, retry_fn = (lambda : self.open_game_throw(practice = True)))
        return None
    msgs = _cancel._minigame_claim('throw', tier)
    self._refresh_minigame_hub()
    self._show_minigame_result_popup(win, False, result_lines + msgs, close_fn = _on_close)
