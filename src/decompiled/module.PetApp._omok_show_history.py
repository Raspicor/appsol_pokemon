# module.PetApp._omok_show_history
# source line 6522
# Recovered from bytecode; default argument values are not shown.

def _omok_show_history(self):
    win = None(self.root)
    win.title('오목 전적')
    resolve_species_win(win, 320, 380)

    try:
        win.attributes('-topmost', True)
        body = None(win)
        body.pack(fill = 'both', expand = True, padx = 12, pady = 12)
        None(body, text = '⚫ 오목 전적', font = ('맑은 고딕', 11, 'bold')).pack(anchor = 'w', pady = (0, 8))
        hist = list(reversed(self.state.get('omok_history', [])))
        None(body, text = '닫기', command = win.destroy).pack(pady = (10, 0))
        self._add_opacity_control(win)
        return None
    except Exception:
        continue
