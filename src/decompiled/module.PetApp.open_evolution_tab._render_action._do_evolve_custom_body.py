# module.PetApp.open_evolution_tab._render_action._do_evolve_custom_body
# source line 8599
# Recovered from bytecode; default argument values are not shown.

def _do_evolve_custom_body():
    if not None('PikaPet', '정말 진화시킬까요? (되돌릴 수 없어요)'):
        return None
    if messagebox.askyesno.evolve_custom_body():
        None()
        return None
    None('PikaPet', '아직 진화 조건을 채우지 못했어요.')
