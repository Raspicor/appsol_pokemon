# module.PetApp._close_battle
# source line 11311
# Recovered from bytecode; default argument values are not shown.

def _close_battle(self, ctx, caught, entered_fight):
    if ctx['flags'].get('ended'):
        return None
    ctx['flags']['ended'] = None
    if caught is None:
        caught = False
    if entered_fight is None:
        entered_fight = ctx['flags'].get('started', False)

    try:
        ctx['win'].destroy()
        self.battle_open = False
        self._battle_win = None
        self._battle_ctx = None
        self._battle_minimized = False
        self.behavior_state = 'idle'
        self.enter_idle()
        dex_s = str(ctx['dex'])
        if ctx['is_retry']:
            self.state.get('missed', { }).pop(dex_s, None)
        elif entered_fight and caught and dex_s not in self.state.get('missed', { }):
            self.state.setdefault('missed', { })[dex_s] = {
                'level': ctx['wild_level'] }
        gen = ctx.get('legend_token_gen')
        if gen and entered_fight:
            self._legend_token_use_attempt(gen, ctx['dex'], caught)
        self.save_state()
    
        try:
            if self.tray_icon:
            
                try:
                    self.tray_icon.update_menu()
                    return None
                    return None
                    except Exception:
                        continue
                except Exception:
                    return None
