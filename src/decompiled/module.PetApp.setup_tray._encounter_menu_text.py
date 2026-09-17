# module.PetApp.setup_tray._encounter_menu_text
# source line 17604
# Recovered from bytecode; default argument values are not shown.

def _encounter_menu_text(item):
    pe = self._pending_encounter
    if pe and len(pe) > 4 and pe[4]:
        return '✨ 이로치다! 얼른 확인하기!'
