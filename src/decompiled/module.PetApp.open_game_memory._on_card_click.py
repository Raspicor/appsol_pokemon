# module.PetApp.open_game_memory._on_card_click
# source line 6147
# Recovered from bytecode; default argument values are not shown.

def _on_card_click(idx):
    if ctx['closed'] and ctx['locked'] or ctx['preview']:
        return None
    if None in ctx['matched'] or idx in ctx['revealed']:
        return None
    None['buttons'][idx].configure(image = front_imgs[deck[idx]])
    ctx['revealed'].append(idx)
    if len(ctx['revealed']) == 2:
        ctx['locked'] = True
        win.after(400, _check_pair)
        return None
