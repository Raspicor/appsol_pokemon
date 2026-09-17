# module.PetApp.open_daily_gift.refresh_gift
# source line 15658
# Recovered from bytecode; default argument values are not shown.

def refresh_gift():
    today = None('%Y-%m-%d')
    if self.state.get('daily_gift_date') == today:
        gift_status_var.set('오늘은 이미 받았어요. 내일 다시 와주세요!')
        gift_btn.configure(text = '오늘은 완료', state = 'disabled')
        return None
    time.strftime.set('아직 오늘의 선물을 안 받으셨어요!')
    gift_btn.configure(text = '🎁 선물 받기', state = 'normal', command = claim_gift)
