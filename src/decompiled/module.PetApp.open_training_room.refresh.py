# module.PetApp.open_training_room.refresh
# source line 15568
# Recovered from bytecode; default argument values are not shown.

def refresh():
    bonus_var.set(f'''누적 공격력 보너스: +{self.train_bonus_pct():.1f}%''')
    today_n = self._train_today_count()
    start = self.state.get('train_session_start', 0)
    if start:
        elapsed = None() - start
        remain = max(0, TRAIN_SESSION_SECONDS - elapsed)
        if remain <= 0:
            status_var.set('훈련 완료! 아래 버튼으로 보상을 받으세요.')
            action_btn.configure(text = '🎁 보상 받기 (+1%)', state = 'normal', command = claim)
            return None
        mm = time.time(remain // 60)
        ss = int(remain % 60)
        status_var.set(f'''훈련 중... 남은 시간 {mm}분 {ss}초''')
        action_btn.configure(text = '훈련 중...', state = 'disabled')
        win.after(1000, refresh)
        return None
    if None >= TRAIN_MAX_PER_DAY:
        status_var.set(f'''오늘의 훈련 횟수를 다 썼어요 ({today_n}/{TRAIN_MAX_PER_DAY}). 내일 다시 와주세요!''')
        action_btn.configure(text = '오늘은 완료', state = 'disabled')
        return None
    None.set(f'''오늘 {today_n}/{TRAIN_MAX_PER_DAY}회 사용''')
    action_btn.configure(text = '▶ 훈련 시작하기 (1시간)', state = 'normal', command = start_session)
