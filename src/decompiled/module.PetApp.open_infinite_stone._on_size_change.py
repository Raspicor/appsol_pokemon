# module.PetApp.open_infinite_stone._on_size_change
# source line 5779
# Recovered from bytecode; default argument values are not shown.

def _on_size_change(_v):
    self.state['infinite_stone_size'] = size_var.get()
    size_val_var.set(f'''{size_var.get()}px''')
    self.save_state()
    None()
