# module.PetApp.open_pokedex._rebuild_slot_bar._toggle_body_visible
# source line 16558
# Recovered from bytecode; default argument values are not shown.

def _toggle_body_visible(key):
    ok = self.set_body_visibility(key, not self.body_visibility(key))
    if not ok:
        None('PikaPet', '본체는 최소 1개는 화면에 보이고 있어야 해요!')
        return None
    None._apply_body1_visibility()
    self._rebuild_body2()
    self.save_state()
    None()
