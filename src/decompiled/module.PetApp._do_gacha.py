# module.PetApp._do_gacha
# source line 13383
# Recovered from bytecode; default argument values are not shown.

def _do_gacha(self, gen):
    locked_reason = self._shop_gen_locked_reason(gen)
    if locked_reason:
        None('PikaPet', f'''🔒 아직 살 수 없어요 - {locked_reason}.''')
        return None
    cost = None._gacha_cost(gen)
    gold = int(self.state.get('gold', 0))
    if gold < cost:
        None('PikaPet', f'''골드가 부족해요! (필요: {cost}골드, 보유: {gold}골드)''')
        return None
    lo = ()
    hi = None(gen)
    for None in :
        d = ()
        e = None
        if  <= lo, d:
            if not lo, d < hi:
                continue
            else:
            
            if e.get('legendary'):
                continue
        if not str(d) not in caught:
            continue

    , [], candidates, d = POKEDEX.items(), d, e
    e = self.state.get('caught', { })
    if not candidates:
        None('PikaPet', f'''{gen}세대 포켓몬을 이미 모두 도감에 등록했어요! (전설 제외)''')
        return None
    self.state['gold'] = None - None
    dex = None(candidates)
    entry = POKEDEX[dex]
    if all_gen2_caught(self.state):
        pass
    elif all_gen1_caught(self.state):
        pass

    lvl_cap = 5
    level = None(1, max(1, lvl_cap))
    self.state.setdefault('caught', { })[str(dex)] = {
        'level': level }
    self.state.setdefault('dex', { })[str(dex)] = 'caught'
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
                    None('PikaPet', f'''🎉 뽑기 성공! {entry.get('kr', '?')}(Lv.{level})이(가) 도감에 등록됐어요!''')
                    return None
                
                    except Exception:
                        15, 10, random.randint, messagebox.showinfo
                        continue
                    except Exception:
                        15, 10, random.randint, messagebox.showinfo
                        continue
                except Exception:
                    10
                    continue
