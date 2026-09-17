# module.PetApp.setup_tray
# source line 17562
# Recovered from bytecode; default argument values are not shown.

def setup_tray(self):
    try:
        import pystray
        self._pystray = pystray
    
        try:
        
            def _recall(icon, item):
                self.force_recall()

        
            def _recall_top_left(icon, item):
                self.force_recall_top_left()

        
            def _recall_primary(icon, item):
                self.force_recall_primary_center()

        
            def _recall_cursor(icon, item):
                self.force_recall_to_cursor()

        
            def _release(icon, item):
                self.exit_ball()

        
            def _status(icon, item):
                self.open_status()

        
            def _open_pokedex(icon, item):
                self.open_pokedex()

        
            def _open_encounter(icon, item):
                self._open_pending_encounter()

        
            def _restore_battle(icon, item):
                self._restore_battle_window()

        
            def _quit(icon, item):
                self.quit_app()

        
            def _open_settings(icon, item):
                self.open_settings()

        
            def _encounter_menu_text(item):
                pe = self._pending_encounter
                if pe and len(pe) > 4 and pe[4]:
                    return '✨ 이로치다! 얼른 확인하기!'

            menu = pystray.Menu(pystray.MenuItem(_encounter_menu_text, _open_encounter, visible = (lambda item: self._pending_encounter is not None)), pystray.MenuItem('⚔ 전투 창 다시 열기', _restore_battle, visible = (lambda item: self._battle_minimized)), pystray.MenuItem('📖 도감 보기 / 동료 장착', _open_pokedex), pystray.MenuItem('📍 지금 불러오기 (화면 중앙)', _recall), pystray.MenuItem('📍 마우스 위치로 부르기 (안 보이면 이거!)', _recall_cursor), pystray.MenuItem('📍 화면 왼쪽 위 구석으로', _recall_top_left), pystray.MenuItem('📍 주 모니터 중앙으로', _recall_primary), pystray.MenuItem('몬스터볼에서 꺼내기', _release, visible = (lambda item: bool(self.state.get('in_ball')))), pystray.MenuItem('상태 보기', _status, visible = (lambda item: not self.state.get('in_ball'))), pystray.MenuItem('⚙ 설정', _open_settings), pystray.MenuItem('종료', _quit))
            icon = pystray.Icon('pikapet', self._tray_image(), 'PikaPet', menu)
            self.tray_icon = icon
            None(target = icon.run, daemon = True).start()
            return None
            except Exception:
                self.tray_icon = None
                self._pystray = None
                return None
        except Exception:
            self.tray_icon = None
            return None
