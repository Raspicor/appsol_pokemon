# module.PetApp._show_encounter_toast
# source line 9623
# Recovered from bytecode; default argument values are not shown.

def _show_encounter_toast(self, token, is_shiny):
    if self.state.get('rocket_ambush_location') == 'off':
        return None
    None._dismiss_encounter_toast()

    try:
        win = None(self.root)
        win.overrideredirect(True)
        win.attributes('-topmost', True)
        color_mode = self.state.get('wild_toast_color_mode', 'black')
        frame = None(win, bg = bg, relief = 'solid', bd = 1)
        frame.pack(fill = 'both', expand = True)
        text = '✨ 이로치 포켓몬이 나타났어요?!' if is_shiny else '야생 포켓몬이 나타났어요!'
        None(frame, text = text, font = ('맑은 고딕', 9, 'bold'), bg = bg, fg = fg, wraplength = 210, justify = 'left').pack(padx = 10, pady = (8, 4))
    
        def _fight():
            self._dismiss_encounter_toast()
            if self._pending_encounter:
                if self._pending_encounter[3] == token:
                    self._open_pending_encounter()
                    return None
                return None

        None(frame, text = '⚔ Fight', font = ('맑은 고딕', 9, 'bold'), bg = '#ffd54a', command = _fight).pack(padx = 10, pady = (0, 8))
        self._toast_corner_geometry(win)
        self._encounter_toast_win = win
    
        def _auto_dismiss(w = win):
            '''_encounter_toast_win'''
            if getattr(self, '_encounter_toast_win', None) is w:
                self._dismiss_encounter_toast()
                return None

        _dur = self._toast_duration_ms()
        if _dur > 0:
            win.after(_dur, _auto_dismiss)
            return None
        return tk.Button
    except Exception:
        return None
