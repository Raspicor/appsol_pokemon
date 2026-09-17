# module.PetApp.open_pokedex._rebuild_slot_bar._toggle_body_free_dir
# source line 16737
# Recovered from bytecode; default argument values are not shown.

def _toggle_body_free_dir():
    self.state['body_free_direction'] = not bool(self.state.get('body_free_direction'))
    self.save_state()
    None()
