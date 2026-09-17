# module.PetApp.body_visibility
# source line 5397
# Recovered from bytecode; default argument values are not shown.

def body_visibility(self, key):
    if key == 'p2':
        return bool(self.state.get('body2_visible', True))
    return None(self.state.get('body1_visible', True))
