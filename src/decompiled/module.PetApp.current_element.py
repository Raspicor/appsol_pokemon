# module.PetApp.current_element
# source line 4844
# Recovered from bytecode; default argument values are not shown.

def current_element(self):
    conf = self.stage_conf()
    if not conf.get('element'):
        conf.get('element')
    return SPECIES[self.state['starter']].get('element', 'normal')
