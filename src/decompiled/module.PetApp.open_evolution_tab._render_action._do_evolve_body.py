# module.PetApp.open_evolution_tab._render_action._do_evolve_body
# source line 8569
# Recovered from bytecode; default argument values are not shown.

def _do_evolve_body():
    if not self.evolution_ready():
        None('PikaPet', '아직 진화 조건을 채우지 못했어요.')
        return None
    if not None('PikaPet', '정말 진화시킬까요? (되돌릴 수 없어요)'):
        return None
    None.askyesno.evolve()
    None()
