# module.PetApp._mega_sprite_id
# source line 6900
# Recovered from bytecode; default argument values are not shown.

def _mega_sprite_id(self):
    if not self.state.get('mega_evolved'):
        return None
    if None.state.get('custom_body_dex'):
        return None
    if not None.state.get('mega_form'):
        None.state.get('mega_form')
    want_form = 'x'
    for None in self.mega_sprite_folder_candidates():
        form = ()
        folder = None
        if form is not None and want_form != form:
            continue
        if not os.path.isdir(sprite_folder_path(folder)):
            continue
        return self.mega_sprite_folder_candidates(), folder
