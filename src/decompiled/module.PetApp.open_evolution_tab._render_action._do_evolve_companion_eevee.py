# module.PetApp.open_evolution_tab._render_action._do_evolve_companion_eevee
# source line 8629
# Recovered from bytecode; default argument values are not shown.

def _do_evolve_companion_eevee(branch, branch_kr, dd):
    if not cstatus.get('ready'):
        None('PikaPet', '아직 진화 조건을 채우지 못했어요.')
        return None
    if not None('PikaPet', f'''정말 {branch_kr}(으)로 진화시킬까요?\n(진화 후에는 되돌릴 수 없어요)'''):
        return None
    if None.askyesno.evolve_companion(dd, forced_branch = branch):
        None()
        return None
    None('PikaPet', '아직 진화 조건을 채우지 못했어요.')
