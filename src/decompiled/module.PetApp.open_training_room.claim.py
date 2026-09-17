# module.PetApp.open_training_room.claim
# source line 15599
# Recovered from bytecode; default argument values are not shown.

def claim():
    if claim_lock['busy']:
        return None
    claim_lock['busy'] = None

    try:
        action_btn.configure(state = 'disabled')
        start = self.state.get('train_session_start', 0)
        if bool(start):
            bool(start)
        session_done = None() - start >= TRAIN_SESSION_SECONDS
        if session_done or self._train_today_count() >= TRAIN_MAX_PER_DAY:
            claim_lock['busy'] = False
            None()
            return None
        self.state['train_atk_bonus_pct'] = time.time.train_bonus_pct() + TRAIN_ATK_BONUS_PER_SESSION
        self.state['train_session_start'] = 0
        self._train_bump_today()
        self.save_state()
        claim_lock['busy'] = False
        None('PikaPet', '훈련 완료! 공격력이 영구히 1% 올랐어요.')
        None()
        return None
    except Exception:
        continue
