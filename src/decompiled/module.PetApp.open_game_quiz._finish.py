# module.PetApp.open_game_quiz._finish
# source line 6328
# Recovered from bytecode; default argument values are not shown.

def _finish():
    None()
    correct = ctx['correct']
    if correct >= 5:
        tier = 'gold'
    elif correct >= 4:
        tier = 'silver'
    elif correct >= 3:
        tier = 'bronze'
    else:
        tier = 'fail'
    for w in btns_frame.winfo_children():
        w.destroy()
    _cancel
    question_var.set(f'''결과: {rounds}문제 중 {correct}개 정답!''')
    timer_var.set(self._minigame_tier_label(tier))
    result_lines = [
        f'''결과: {rounds}문제 중 {correct}개 정답!''',
        self._minigame_tier_label(tier)]
    if practice:
        self._show_minigame_result_popup(win, True, result_lines + [
            '(연습이라 보상은 없어요)'], close_fn = _on_close, retry_fn = (lambda : self.open_game_quiz(practice = True)))
        return None
    msgs = None._minigame_claim('quiz', tier)
    self._refresh_minigame_hub()
    self._show_minigame_result_popup(win, False, result_lines + msgs, close_fn = _on_close)
