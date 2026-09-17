# module.PetApp.open_game_throw
# source line 6356
# Recovered from bytecode; default argument values are not shown.

def open_game_throw(self, practice):
    if practice and self._minigame_played_today('throw'):
        None('PikaPet', "오늘은 이미 '몬스터볼 조준' 도전을 마쳤어요. 내일 다시 도전해보세요!\n(연습하기는 계속 하실 수 있어요.)")
        return None
    if None._minigame_window_active():
        None('PikaPet', '이미 다른 미니게임 창이 열려 있어요! 먼저 그 창을 닫아주세요.')
        return None
    if not None:
        self._warn_challenge_start()
    win = None(self.root)
    win.title('몬스터볼 조준 던지기' + ' (연습)' if practice else ' (도전!)')
    resolve_species_win(win, 340, 380)
    self._active_minigame_win = win
    if not practice:
        self._mark_minigame_started('throw')
    ctx = {
        'resolved': True,
        'zone_w': 60,
        'zone_start': 100,
        'speed': 4,
        'dir': 1,
        'pos': 20,
        'hits': 0,
        'rounds': 5,
        'round': 0,
        'closed': False,
        'job': None }

    def _cancel():
        '''job'''
        if ctx['job'] is not None:
        
            try:
                win.after_cancel(ctx['job'])
                ctx['job'] = None
                return None
                return None
            except Exception:
                continue



    def _on_close():
        ctx['closed'] = True
        None()
        self._clear_active_minigame_win(win)
        win.destroy()

    win.protocol('WM_DELETE_WINDOW', _on_close)
    self._add_opacity_control(win)
    None(win, text = '🎯 몬스터볼이 초록 영역 위에 있을 때 클릭하세요!', font = ('맑은 고딕', 10, 'bold')).pack(pady = (10, 2))
    status_var = None(value = '')
    None(win, textvariable = status_var, font = ('맑은 고딕', 9), fg = '#555').pack(pady = (0, 4))
    canvas = None(win, width = 300, height = 140, bg = '#eef7ea', highlightthickness = 1, highlightbackground = '#ccc')
    canvas.pack(padx = 10, pady = 6)
    bar_y = 90
    left_x, right_x = 20, 280

    def _step():
        '''closed'''
        if ctx['closed']:
            return None
        None.delete('all')
        canvas.create_rectangle(left_x, bar_y - 6, right_x, bar_y + 6, outline = '#999')
        zs = ctx['zone_start']
        canvas.create_rectangle(zs, bar_y - 6, zs + ctx['zone_w'], bar_y + 6, fill = '#8be07a', outline = '')
        canvas.create_oval(ctx['pos'] - 8, bar_y - 8, ctx['pos'] + 8, bar_y + 8, fill = '#e33333', outline = '#900000', width = 2, tags = 'ball')
        if ctx['pos'] >= right_x:
            right_x = None
            ctx['dir'] = -1
        elif ctx['pos'] <= left_x:
            ctx['pos'] = left_x
            ctx['dir'] = 1
        ctx['job'] = win.after(20, _step)


    def _resolve():
        '''resolved'''
        if ctx['resolved']:
            return None
        ctx['resolved'] = None
        None()
        zs = ctx['zone_start']
        if  <= zs, ctx['pos'] or zs, ctx['pos'] <= zs + ctx['zone_w']:
            pass
        else:
            _cancel
        win.after(300, _new_round)


    def _on_click(evt):
        '''closed'''
        if ctx['closed'] and ctx['resolved'] or ctx['round'] == 0:
            return None
        None()

    canvas.bind('<Button-1>', _on_click)

    def _new_round():
        '''closed'''
        if ctx['closed']:
            return None
        if None['round'] >= ctx['rounds']:
            None()
            return None
        max(28, 60 - (ctx['round'] - 1) * 7) = None
        ctx['zone_w'] = zone_w
        ctx['zone_start'] = None(left_x, right_x - zone_w)
        ctx['pos'] = left_x
        ctx['dir'] = 1
        ctx['speed'] = 4 + (ctx['round'] - 1) * 0.4
        ctx['resolved'] = False
        status_var.set(f'''{ctx['round']}/{ctx['rounds']}라운드  ·  성공 {ctx['hits']}개''')
        None()
        None()


    def _finish():
        '''hits'''
        None()
        hits = ctx['hits']
        if hits >= 5:
            tier = 'gold'
        elif hits >= 4:
            tier = 'silver'
        elif hits >= 2:
            tier = 'bronze'
        else:
            tier = 'fail'
        canvas.delete('all')
        canvas.create_text(150, 60, text = f'''결과: {hits}/{ctx['rounds']}개 성공''', font = ('맑은 고딕', 13, 'bold'))
        canvas.create_text(150, 90, text = self._minigame_tier_label(tier), font = ('맑은 고딕', 12))
        result_lines = [
            f'''결과: {hits}/{ctx['rounds']}개 성공''',
            self._minigame_tier_label(tier)]
        if practice:
            self._show_minigame_result_popup(win, True, result_lines + [
                '(연습이라 보상은 없어요)'], close_fn = _on_close, retry_fn = (lambda : self.open_game_throw(practice = True)))
            return None
        msgs = _cancel._minigame_claim('throw', tier)
        self._refresh_minigame_hub()
        self._show_minigame_result_popup(win, False, result_lines + msgs, close_fn = _on_close)

    None()
