# module.PetApp._grant_legend_ticket_pokemon
# source line 14742
# Recovered from bytecode; default argument values are not shown.

def _grant_legend_ticket_pokemon(self, gen, dex):
    tickets = self.state.setdefault('legend_tickets', { })
    key = str(gen)
    if int(tickets.get(key, 0)) <= 0:
        return None
    tickets[key] = None(tickets.get(key, 0)) - 1
    entry = POKEDEX.get(dex, { })
    level = 5
    self.state.setdefault('caught', { })[str(dex)] = {
        'level': level }
    self.state.setdefault('dex', { })[str(dex)] = 'caught'
    self._clear_legend_token_for_dex(dex)
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
                    None('PikaPet', f'''🎉 전설 선택권 사용! {entry.get('kr', '?')}(Lv.{level})이(가) 도감에 등록됐어요!''')
                    return None
                    except Exception:
                        continue
                    except Exception:
                        continue
                except Exception:
                    continue
