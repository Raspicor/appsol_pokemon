# module.PetApp.open_mining._offer_replay_or_close
# source line 12116
# Recovered from bytecode; default argument values are not shown.

def _offer_replay_or_close():
    remaining = MINE_MAX_PER_DAY - self._mine_today_count()
    if remaining > 0:
    
        try:
            replay_btn.configure(text = f'''▶ 한 번 더 하기 (오늘 {remaining}회 남음)''')
            replay_btn.pack(pady = (6, 0))
            return None
        
            try:
                close_btn.configure(text = '닫기')
                close_btn.pack(pady = (6, 0))
                return None
                except Exception:
                    return None
            except Exception:
                return None
