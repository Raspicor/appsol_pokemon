# module.PetApp._minimize_battle
# source line 10379
# Recovered from bytecode; default argument values are not shown.

def _minimize_battle(self, ctx):
    try:
        ctx['win'].withdraw()
        self._battle_minimized = True
    
        try:
            if self.tray_icon:
            
                try:
                    self.tray_icon.update_menu()
                    self.tray_icon.notify('전투가 계속되고 있어요. 트레이 아이콘을 눌러 다시 열 수 있어요.', 'PikaPet')
                    return None
                    return None
                    except Exception:
                        continue
                except Exception:
                    return None
