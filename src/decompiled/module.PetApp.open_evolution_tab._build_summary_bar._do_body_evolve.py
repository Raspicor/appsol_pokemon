# module.PetApp.open_evolution_tab._build_summary_bar._do_body_evolve
# source line 8979
# Recovered from bytecode; default argument values are not shown.

def _do_body_evolve():
    if not None('PikaPet', '정말 진화시킬까요? (되돌릴 수 없어요)'):
        return None
    messagebox.askyesno.evolve()
    None()
