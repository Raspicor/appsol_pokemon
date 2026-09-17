# module.PetApp._pvp_my_party_names
# source line 17639
# Recovered from bytecode; default argument values are not shown.

def _pvp_my_party_names(self):
    names = []

    try:
        dex1 = self.player_dex()
        if dex1:
        
            try:
                names.append(POKEDEX.get(dex1, { }).get('kr', f'''#{dex1}''') + '(본체)')
            
                try:
                    dex2 = self.state.get('second_body_dex')
                    if dex2:
                    
                        try:
                            names.append(POKEDEX.get(dex2, { }).get('kr', f'''#{dex2}''') + '(본체2)')
                        
                            try:
                                cap = companion_slot_count(self.state)
                                for d in list(self.state.get('party', []))[:cap]:
                                    names.append(POKEDEX.get(d, { }).get('kr', f'''#{d}'''))
                                return names
                                except Exception:
                                    continue
                                except Exception:
                                    continue
                            except Exception:
                                return names
