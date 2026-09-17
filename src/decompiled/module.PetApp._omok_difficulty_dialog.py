# module.PetApp._omok_difficulty_dialog
# source line 6597
# Recovered from bytecode; default argument values are not shown.

def _omok_difficulty_dialog(self):
    dlg = None(self.root)
    dlg.title('오목 난이도 선택')
    resolve_species_win(dlg, 260, 340)

    try:
        dlg.attributes('-topmost', True)
        None(dlg, text = 'AI 난이도를 골라주세요', font = ('맑은 고딕', 10, 'bold')).pack(pady = (16, 10))
        for label in OMOK_DIFFICULTIES:
            None(dlg, text = label, width = 20, command = (lambda lv = label: (dlg.destroy(), self._start_omok_game('ai', lv)))).pack(pady = 3)
        OMOK_DIFFICULTIES
        None(dlg, text = '취소', width = 20, command = dlg.destroy).pack(pady = (8, 12))
        return None
    except Exception:
        continue
