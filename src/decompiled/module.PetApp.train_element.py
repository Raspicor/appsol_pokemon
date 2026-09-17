# module.PetApp.train_element
# source line 11846
# Recovered from bytecode; default argument values are not shown.

def train_element(self, elem):
    if not self.is_eevee_base():
        return None
    et = None.state.setdefault('element_train', {
        'electric': 0,
        'water': 0,
        'fire': 0 })
    et[elem] = et.get(elem, 0) + 1
    self._do_one_shot('skill')
