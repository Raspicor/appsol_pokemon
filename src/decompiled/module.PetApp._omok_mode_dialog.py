# module.PetApp._omok_mode_dialog
# source line 6575
# Recovered from bytecode; default argument values are not shown.

def _omok_mode_dialog(self):
    dlg = None(self.root)
    dlg.title('오목')
    resolve_species_win(dlg, 260, 170)

    try:
        dlg.attributes('-topmost', True)
        None(dlg, text = '⚫ 오목 - 몇 명이서 둘까요?', font = ('맑은 고딕', 10, 'bold')).pack(pady = (16, 12))
    
        def pick_1p():
            dlg.destroy()
            self._omok_difficulty_dialog()

    
        def pick_2p():
            '''2p'''
            dlg.destroy()
            self._start_omok_game('2p')

        None(dlg, text = '1인 (AI와 대전)', width = 20, command = pick_1p).pack(pady = 4)
        None(dlg, text = '2인 (한 화면에서 번갈아 두기)', width = 20, command = pick_2p).pack(pady = 4)
        None(dlg, text = '취소', width = 20, command = dlg.destroy).pack(pady = (6, 12))
        return None
    except Exception:
        continue
