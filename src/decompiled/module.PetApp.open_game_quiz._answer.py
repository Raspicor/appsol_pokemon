# module.PetApp.open_game_quiz._answer
# source line 6266
# Recovered from bytecode; default argument values are not shown.

def _answer(chosen_dex):
    if ctx['closed'] or ctx['answered']:
        return None
    ctx['answered'] = None
    None()
    reveal_img = self._sprite_preview_image(ctx['current_correct_dex'], size = 90)
    win.images.append(reveal_img)
    sil_label.configure(image = reveal_img)
    if chosen_dex == ctx['current_correct_dex']:
        timer_var.set('정답!')
    else:
        POKEDEX.get(ctx['current_correct_dex'], { }).get('kr', '?') = _cancel
        timer_var.set(f'''오답! 정답은 \'{correct_name}\'''')
    for w in btns_frame.winfo_children():
        w.configure(state = 'disabled')
    win.after(900, _new_round)
    return None
    except Exception:
        continue
