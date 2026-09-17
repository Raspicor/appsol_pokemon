# module.PetApp.open_game_memory._preview_tick
# source line 6158
# Recovered from bytecode; default argument values are not shown.

def _preview_tick():
    if ctx['closed']:
        return None
    if None['preview_remaining'] <= 0:
        ctx['preview'] = False
        for btn in ctx['buttons'].values():
            btn.configure(image = back_img)
        status_var.set('실수 0회 · 이제 같은 카드를 찾아보세요!')
        return None
    None.set(f'''카드를 잘 기억하세요! {ctx['preview_remaining']}초 후 시작...''')
    win.after(1000, _preview_tick) = None
    return None
    except Exception:
        continue
