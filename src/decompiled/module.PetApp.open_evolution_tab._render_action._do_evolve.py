# module.PetApp.open_evolution_tab._render_action._do_evolve
# source line 8525
# Recovered from bytecode; default argument values are not shown.

def _do_evolve(branch, branch_kr):
    if not self.evolution_ready():
        None('PikaPet', '아직 진화 조건을 채우지 못했어요.')
        return None
    if not None('PikaPet', f'''정말 {branch_kr}(으)로 진화시킬까요?\n(진화 후에는 되돌릴 수 없어요)'''):
        return None
    None.askyesno.evolve(forced_branch = branch)
    None()
