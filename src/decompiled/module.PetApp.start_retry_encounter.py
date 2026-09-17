# module.PetApp.start_retry_encounter
# source line 9719
# Recovered from bytecode; default argument values are not shown.

def start_retry_encounter(self, dex, level):
    entry = POKEDEX.get(int(dex))
    if not entry:
        return None
    if None.battle_open or self._pending_encounter:
        None('PikaPet', '지금은 다른 조우가 진행 중이에요.')
        return None
    self.behavior_state = None
    self.battle_open = True
    gen = legend_gen_for_dex(int(dex)) if entry.get('legendary') else None
    bundle = self._legend_bundle_for_dex(gen, dex) if gen else None
    token_gen = gen if bundle else None

    try:
        self.open_battle(entry, level, is_retry = True, legend_token_gen = token_gen)
        return None
    except Exception:
        self.battle_open = False
        self.behavior_state = 'idle'
        self.enter_idle()
        return None
