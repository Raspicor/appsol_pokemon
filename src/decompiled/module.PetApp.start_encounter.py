# module.PetApp.start_encounter
# source line 9354
# Recovered from bytecode; default argument values are not shown.

def start_encounter(self):
    try:
        entry = ()
        level = pick_wild(self.effective_wild_center_level(), gen1_complete = all_gen1_caught(self.state), gen2_complete = all_gen2_caught(self.state), gen3_complete = all_gen3_caught(self.state), gen4_complete = all_gen4_caught(self.state))
        if not entry:
            return None
        self.state.get('encounter_notify_mode', 'blink') = None() < SHINY_CHANCE * title_shiny_chance_mult(self.state)
        if not mode == 'blink' and self.tray_icon:
            mode = 'popup'
        if mode == 'popup':
            self.behavior_state = 'acting'
            self.battle_open = True
        
            try:
                self.open_battle(entry, level, is_shiny = is_shiny)
                return None
                token = None()
                self._pending_encounter = (entry, level, False, token, is_shiny)
                self._start_blink()
            
                try:
                    if self.tray_icon:
                        self.tray_icon.update_menu()
                        if mode != 'toast':
                            if is_shiny:
                            
                                try:
                                    pass
                                notify_text = '야생 포켓몬이 나타난 것 같아요!\n트레이 아이콘을 클릭해 확인해보세요.'
                                self.root.after(ENCOUNTER_IGNORE_TIMEOUT_MS, (lambda t = token: self._encounter_timeout(t)))
                                if mode == 'toast':
                                    self._show_encounter_toast(token, is_shiny)
                                    return None
                                return '✨ 이로치 포켓몬이 나타났어요?! 얼른 확인해보세요!'
                                except Exception:
                                    None.random
                                    level = 1
                                    entry = None
                                    continue

                                except Exception:
                                    None.random
                                    self.battle_open = False
                                    self.behavior_state = 'idle'
                                    self.enter_idle()
                                    return None
                                except Exception:
                                    None.random
                                    continue
