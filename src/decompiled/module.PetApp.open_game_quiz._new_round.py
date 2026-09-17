# module.PetApp.open_game_quiz._new_round
# source line 6288
# Recovered from bytecode; default argument values are not shown.

def _new_round():
    if ctx['closed']:
        return None
    if None['round'] >= rounds:
        None()
        return None
    idx = None['round']
    quiz_dex[idx] = None
    entry = POKEDEX.get(dex, { })
    correct_name = entry.get('kr', f'''#{dex}''')
    if not entry.get('desc'):
        entry.get('desc')
    desc = ''
    elem = entry.get('element', '')
    clue = desc if desc else f'''타입: {elem}'''
    question_var.set(f'''[{ctx['round']}/{rounds}번] {clue}''')
    status_var.set(f'''맞힌 개수: {ctx['correct']}개''')
    sil_img = self._sprite_preview_image(dex, size = 90, silhouette = True)
    win.images.append(sil_img)
    sil_label.configure(image = sil_img)
    for None in :
        d = None
        if not d != dex:
            continue

    , [], wrong_pool, d = all_dex, d
    None(wrong_pool)
    wrong_dex = wrong_pool[<TYPE: 58>
    ]
    for None in :
        d = None

    wrong_dex, d, , [] + d, = [
        (dex, correct_name)]
    None(options)
    for w in btns_frame.winfo_children():
        w.destroy()
    random.shuffle
    ctx['answered'] = False
    ctx['remaining'] = time_limit
    ctx['current_correct_dex'] = dex
    timer_var.set(f'''남은 시간: {time_limit}초''')
    for None in options:
        opt_dex = ()
        opt_name = None
    options
    None()
    return None
