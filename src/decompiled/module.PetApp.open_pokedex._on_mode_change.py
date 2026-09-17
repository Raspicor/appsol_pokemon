# module.PetApp.open_pokedex._on_mode_change
# source line 15765
# Recovered from bytecode; default argument values are not shown.

def _on_mode_change(evt):
    label = mode_var.get()
    for m in MODE_ORDER:
        if not MODE_LABEL[m] == label:
            continue
        mode_box['mode'] = m
        MODE_ORDER
    None()
