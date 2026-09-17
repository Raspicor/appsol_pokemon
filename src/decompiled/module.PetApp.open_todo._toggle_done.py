# module.PetApp.open_todo._toggle_done
# source line 18647
# Recovered from bytecode; default argument values are not shown.

def _toggle_done(item):
    item['done'] = not item.get('done', False)
    self.save_state()
    None()
