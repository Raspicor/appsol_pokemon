# module.PetApp.set_body_visibility
# source line 5402
# Recovered from bytecode; default argument values are not shown.

def set_body_visibility(self, key, visible):
    if visible:
        if key == 'p2':
            self.state['body2_visible'] = True
            return True
        self.state['body1_visible'] = None
        return True
    if None == 'p2':
        other_ok = self.body_visibility('p1')
    elif bool(second_body_equipped_dex(self.state)):
        bool(second_body_equipped_dex(self.state))
    other_ok = self.body_visibility('p2')
    if not other_ok:
        return False
    if None == 'p2':
        self.state['body2_visible'] = False
        return True
    self.state['body1_visible'] = None
    return True
