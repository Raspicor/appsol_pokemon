# module.PetApp._daily_gift_claim
# source line 13851
# Recovered from bytecode; default argument values are not shown.

def _daily_gift_claim(self):
    today = None('%Y-%m-%d')
    if self.state.get('daily_gift_date') == today:
        return (False, '오늘은 이미 받았어요. 내일 다시 와주세요!')
    picked = time.strftime._daily_gift_pick()
    if picked is None:
        self.state['daily_gift_date'] = today
        self.save_state()
        return (False, '지금은 드릴 미보유 포켓몬이 없어요 - 이미 다 모으셨나 봐요! 대단해요 🎉')
    gen = ()
    dex = None
    if all_gen2_caught(self.state):
        pass
    elif all_gen1_caught(self.state):
        pass

    5 = 10
    level = None(1, max(1, lvl_cap))
    self.state.setdefault('caught', { })[str(dex)] = {
        'level': level }
    self.state.setdefault('dex', { })[str(dex)] = 'caught'
    self.state['daily_gift_date'] = today
    prev_player_level = player_level_from_state(self.state)
    record_catch_for_leveling(self.state, level)
    if player_level_from_state(self.state) > prev_player_level:
    
        try:
            self.trigger_fx('levelup')
        
            try:
                self.check_companion_leveling()
                self.save_state()
            
                try:
                    self._check_and_show_gen_certificates()
                    is_legend = bool(entry.get('legendary'))
                    star = ' ⭐전설이에요!!' if is_legend else ''
                    return (True, f'''🎁 도형님이 주는 일일선물: {entry.get('kr', '?')}(Lv.{level})이(가) 도착했어요!{star}''')
                    except Exception:
                        15
                        continue
                    except Exception:
                        15
                        continue
                except Exception:
                    15
                    continue
