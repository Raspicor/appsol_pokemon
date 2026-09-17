# module.PetApp._restore_battle_window
# source line 10392
# Recovered from bytecode; default argument values are not shown.

def _restore_battle_window(self):
    if not self._battle_ctx or self._battle_win:
        return None

    try:
        self._battle_win.deiconify()
        self._battle_win.lift()
        self._battle_win.attributes('-topmost', True)
        self._battle_minimized = False
    
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
