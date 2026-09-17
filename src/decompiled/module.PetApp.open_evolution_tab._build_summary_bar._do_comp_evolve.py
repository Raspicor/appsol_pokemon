# module.PetApp.open_evolution_tab._build_summary_bar._do_comp_evolve
# source line 8997
# Recovered from bytecode; default argument values are not shown.

def _do_comp_evolve(dd):
    if not None('PikaPet', f'''정말 {POKEDEX.get(dd, { }).get('kr', '?')}을(를) 진화시킬까요?'''):
        return None
    if messagebox.askyesno.evolve_companion(dd):
        None()
        return None
