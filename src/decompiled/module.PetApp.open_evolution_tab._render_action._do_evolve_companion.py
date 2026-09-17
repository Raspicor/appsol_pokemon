# module.PetApp.open_evolution_tab._render_action._do_evolve_companion
# source line 8684
# Recovered from bytecode; default argument values are not shown.

def _do_evolve_companion(dd):
    if not None('PikaPet', f'''정말 {POKEDEX.get(dd, { }).get('kr', '?')}을(를) 진화시킬까요?'''):
        return None
    if messagebox.askyesno.evolve_companion(dd):
        None()
        return None
    None('PikaPet', '아직 진화 조건을 채우지 못했어요.')
