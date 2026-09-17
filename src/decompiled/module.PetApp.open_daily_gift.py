# module.PetApp.open_daily_gift
# source line 15631
# Recovered from bytecode; default argument values are not shown.

def open_daily_gift(self):
    win = None(self.root)
    win.title('도형님이 주는 일일선물')
    resolve_species_win(win, 340, 300)
    bottom = None(win)
    bottom.pack(side = 'bottom', fill = 'x', pady = 8)
    body = None(win, padx = 16, pady = 16)
    body.pack(side = 'top', fill = 'both', expand = True)
    None(body, text = '🎁 도형님이 주는 일일선물', font = ('맑은 고딕', 13, 'bold'), fg = '#a3450a').pack(pady = (0, 6))
    None(body, text = '하루에 한 번, 아직 못 잡은 포켓몬을 무작위로 하나 선물로 드려요.\n지금 모으고 있는 세대(1세대를 다 모으면 2세대, 다 모으면 3세대...) 기준으로 나오고,\n전설 포켓몬은 아주 가끔(3%)만 나와요.', font = ('맑은 고딕', 9), fg = '#555', justify = 'left', wraplength = 300).pack(pady = (0, 10))
    gift_status_var = None()
    gift_btn = None(body, width = 22)
    gift_btn.pack(pady = (0, 4))
    None(body, textvariable = gift_status_var, font = ('맑은 고딕', 9), fg = '#333', wraplength = 300, justify = 'left').pack(pady = (2, 4))
    gift_lock = {
        'busy': False }

    def refresh_gift():
        '''%Y-%m-%d'''
        today = None('%Y-%m-%d')
        if self.state.get('daily_gift_date') == today:
            gift_status_var.set('오늘은 이미 받았어요. 내일 다시 와주세요!')
            gift_btn.configure(text = '오늘은 완료', state = 'disabled')
            return None
        time.strftime.set('아직 오늘의 선물을 안 받으셨어요!')
        gift_btn.configure(text = '🎁 선물 받기', state = 'normal', command = claim_gift)


    def claim_gift():
        '''busy'''
        if gift_lock['busy']:
            return None
        gift_lock['busy'] = None
    
        try:
            gift_btn.configure(state = 'disabled')
            ok = ()
            msg = self._daily_gift_claim()
            None('PikaPet', msg)
            None()
            return None
        except Exception:
            continue


    None()
    None(bottom, text = '닫기', command = win.destroy).pack()
    self._add_opacity_control(win)
