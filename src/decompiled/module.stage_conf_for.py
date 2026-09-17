# module.stage_conf_for
# source line 849
# Recovered from bytecode; default argument values are not shown.

def stage_conf_for(state):
    sp = SPECIES[state['starter']]
    stage = state.get('stage', 0)
    if sp.get('branching'):
        if stage <= 0:
            return sp['stages'][0]
        if not None.get('eevee_branch'):
            None.get('eevee_branch')
        branch = 'water'
        return sp['branches'][branch]
    idx = None(0, min(stage, len(sp['stages']) - 1))
    return sp['stages'][idx]
