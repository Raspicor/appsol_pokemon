# module.PetApp._inf_free_gacha_grant
# source line 14594
# Recovered from bytecode; default argument values are not shown.

def _inf_free_gacha_grant(self, gen):
    lo = ()
    hi = gen_dex_range(gen)
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
        return None
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
            
                try:
                    self._check_and_show_gen_certificates()
                    return f'''🎁 무료 뽑기: {entry.get('kr', '?')}(Lv.{level})이(가) 도감에 등록됐어요!'''
                
                    except Exception:
                        None.choice, 15, 10, random.randint
                        continue
                    except Exception:
                        None.choice, 15, 10, random.randint
                        continue
                except Exception:
                    10
                    continue
