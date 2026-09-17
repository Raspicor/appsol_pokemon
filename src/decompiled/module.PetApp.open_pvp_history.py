# module.PetApp.open_pvp_history
# source line 17926
# Recovered from bytecode; default argument values are not shown.

def open_pvp_history(self):
    if getattr(self, '_pvp_history_win', None) is not None:
    
        try:
            self._pvp_history_win.lift()
            return None
            win = None(self.root)
            self._pvp_history_win = win
            win.title('📜 온라인 대결 기록')
        
            try:
                win.attributes('-topmost', True)
                resolve_species_win(win, 380, 440)
                body = None(win, padx = 12, pady = 10)
                body.pack(fill = 'both', expand = True)
                None(body, text = '📜 온라인 대결 기록', font = ('맑은 고딕', 12, 'bold')).pack(pady = (0, 8))
                log = list(reversed(self.state.get('pvp_battle_log', [])))
            
                def _on_close():
                    self._pvp_history_win = None
                    win.destroy()

                win.protocol('WM_DELETE_WINDOW', _on_close)
                None(body, text = '닫기', command = _on_close).pack(pady = (10, 0))
                self._add_opacity_control(win)
                return None
                except Exception:
                    log if not log else '#1a7a2a'
                    continue
            except Exception:
                continue
