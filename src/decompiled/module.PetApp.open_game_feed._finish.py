# module.PetApp.open_game_feed._finish
# source line 5978
# Recovered from bytecode; default argument values are not shown.

def _finish():
    None()
    hits = ctx['hits']
    if hits >= 9:
        tier = 'gold'
    elif hits >= 6:
        tier = 'silver'
    elif hits >= 3:
        tier = 'bronze'
    else:
        tier = 'fail'
    canvas.delete('all')
    canvas.create_text(150, 130, text = f'''결과: {hits}/{ctx['rounds']}개 받음''', font = ('맑은 고딕', 13, 'bold'))
    canvas.create_text(150, 160, text = self._minigame_tier_label(tier), font = ('맑은 고딕', 12))
    result_lines = [
        f'''결과: {hits}/{ctx['rounds']}개 받음''',
        self._minigame_tier_label(tier)]
    if practice:
        self._show_minigame_result_popup(win, True, result_lines + [
            '(연습이라 보상은 없어요)'], close_fn = _on_close, retry_fn = (lambda : self.open_game_feed(practice = True)))
        return None
    reward_msgs = _cancel
    if tier == 'gold':
        self.state['hunger'] = 100
        self.state['affection'] = min(100, self.state.get('affection', 50) + 15)
        self.state['encounter_boost_until'] = None() + 3600
        reward_msgs.append('배고픔 완전 회복 + 애정도 +15 + 1시간 동안 야생 조우 확률 1.5배!')
    elif tier == 'silver':
        self.state['hunger'] = 100
        self.state['affection'] = min(100, self.state.get('affection', 50) + 10)
        reward_msgs.append('배고픔 완전 회복 + 애정도 +10')
    elif tier == 'bronze':
        self.state['hunger'] = min(100, self.state.get('hunger', 80) + 40)
        self.state['affection'] = min(100, self.state.get('affection', 50) + 5)
        reward_msgs.append('배고픔 절반 회복 + 애정도 +5')
    else:
        self.state['affection'] = min(100, self.state.get('affection', 50) + 2)
        reward_msgs.append('참가상: 애정도 +2')
    msgs = self._minigame_claim('feed', tier, extra_msgs = reward_msgs)
    self.save_state()
    self._refresh_minigame_hub()
    self._show_minigame_result_popup(win, False, result_lines + msgs, close_fn = _on_close)
