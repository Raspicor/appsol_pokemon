# module.PetApp.check_evolution
# source line 7507
# Recovered from bytecode; default argument values are not shown.

def check_evolution(self):
    self._maybe_notify_mega_intro()
    if not self.evolution_ready():
        return None
    if None in self.state.get('evolve_ready_notified', []):
        return None
    None._notify_evolution_ready('body', f'''{self.display_name()}이(가) 진화할 준비가 됐어요!\n우클릭 메뉴의 \'🧬 진화/레벨 탭\'에서 진화시켜보세요.''')
