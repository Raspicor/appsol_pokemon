# module.PetApp.open_evolution_tab._build_summary_bar._do_custom_body_evolve
# source line 8988
# Recovered from bytecode; default argument values are not shown.

def _do_custom_body_evolve():
    if not None('PikaPet', '정말 진화시킬까요? (되돌릴 수 없어요)'):
        return None
    if messagebox.askyesno.evolve_custom_body():
        None()
        return None
