# module.PetApp.open_game_feed
# source line 5884
# Recovered from bytecode; default argument values are not shown.

def open_game_feed(self, practice):
    if practice and self._minigame_played_today('feed'):
        None('PikaPet', "오늘은 이미 '먹이 받기' 도전을 마쳤어요. 내일 다시 도전해보세요!\n(연습하기는 계속 하실 수 있어요.)")
        return None
    if None._minigame_window_active():
        None('PikaPet', '이미 다른 미니게임 창이 열려 있어요! 먼저 그 창을 닫아주세요.')
        return None
    if not None:
        self._warn_challenge_start()
    win = None(self.root)
    win.title('먹이 받기' + ' (연습)' if practice else ' (도전!)')
    resolve_species_win(win, 340, 430)
    self._active_minigame_win = win
    if not practice:
        self._mark_minigame_started('feed')
    ctx = {
        'resolved': True,
        'speed': 130,
        'radius': 20,
        'item_y': 0,
        'item_x': 0,
        'item': None,
        'rounds': 10,
        'hits': 0,
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
    None(win, text = '🍎 떨어지는 먹이를 클릭해서 받아주세요!', font = ('맑은 고딕', 10, 'bold')).pack(pady = (10, 2))
    status_var = None(value = '')
    None(win, textvariable = status_var, font = ('맑은 고딕', 9), fg = '#555').pack(pady = (0, 4))
    canvas = None(win, width = 300, height = 300, bg = '#eaf6ff', highlightthickness = 1, highlightbackground = '#ccc')
    canvas.pack(padx = 10, pady = 4)
    floor_y = 280

    def _new_round():
        '''closed'''
        if ctx['closed']:
            return None
        if None['round'] >= ctx['rounds']:
            None()
            return None
        None(30, 270) = random.randint
        ctx['item_y'] = 10
        ctx['radius'] = 16 if ctx['round'] > ctx['rounds'] - 3 else 20
        ctx['speed'] = 130 + (ctx['round'] - 1) * 9
        ctx['resolved'] = False
        status_var.set(f'''{ctx['round']}/{ctx['rounds']}라운드  ·  받은 개수 {ctx['hits']}개''')
        None(first = True)


    def _step(first = False):
        '''closed'''
        if ctx['closed']:
            return None
        None.delete('all')
        canvas.create_line(0, floor_y, 300, floor_y, fill = '#bbb', width = 2)
        canvas.create_oval(ctx['item_x'] - ctx['radius'], ctx['item_y'] - ctx['radius'], ctx['item_x'] + ctx['radius'], ctx['item_y'] + ctx['radius'], fill = '#ff5a5a', outline = '#a02020', width = 2, tags = 'item')
        canvas.create_text(ctx['item_x'], ctx['item_y'], text = '🍎', font = ('맑은 고딕', 14))
        if ctx['item_y'] >= floor_y:
            None(False)
            return None
        win.after(30, _step) = None


    def _resolve(hit):
        '''resolved'''
        if ctx['resolved']:
            return None
        ctx['resolved'] = None
        None()
        if hit:
            pass
        win.after(280, _new_round)


    def _on_click(evt):
        '''closed'''
        if ctx['closed'] and ctx['resolved'] or ctx['round'] == 0:
            return None
        dx = None.x - ctx['item_x']
        dy = evt.y - ctx['item_y']
        if (dx * dx + dy * dy) ** 0.5 <= ctx['radius'] + 6:
            None(True)
            return None

    canvas.bind('<Button-1>', _on_click)

    def _finish():
        '''hits'''
        None()
        hits = ctx['hits']
        if hits >= 9:
            tier = 'gold'
        elif hits >= 6:
            tier = 'silver'
        elif hits >= 3:
            tier = 'bronze'
        else:
            tier = 'fail'
        canvas.delete('all')
        canvas.create_text(150, 130, text = f'''결과: {hits}/{ctx['rounds']}개 받음''', font = ('맑은 고딕', 13, 'bold'))
        canvas.create_text(150, 160, text = self._minigame_tier_label(tier), font = ('맑은 고딕', 12))
        result_lines = [
            f'''결과: {hits}/{ctx['rounds']}개 받음''',
            self._minigame_tier_label(tier)]
        if practice:
            self._show_minigame_result_popup(win, True, result_lines + [
                '(연습이라 보상은 없어요)'], close_fn = _on_close, retry_fn = (lambda : self.open_game_feed(practice = True)))
            return None
        reward_msgs = _cancel
        if tier == 'gold':
            self.state['hunger'] = 100
            self.state['affection'] = min(100, self.state.get('affection', 50) + 15)
            self.state['encounter_boost_until'] = None() + 3600
            reward_msgs.append('배고픔 완전 회복 + 애정도 +15 + 1시간 동안 야생 조우 확률 1.5배!')
        elif tier == 'silver':
            self.state['hunger'] = 100
            self.state['affection'] = min(100, self.state.get('affection', 50) + 10)
            reward_msgs.append('배고픔 완전 회복 + 애정도 +10')
        elif tier == 'bronze':
            self.state['hunger'] = min(100, self.state.get('hunger', 80) + 40)
            self.state['affection'] = min(100, self.state.get('affection', 50) + 5)
            reward_msgs.append('배고픔 절반 회복 + 애정도 +5')
        else:
            self.state['affection'] = min(100, self.state.get('affection', 50) + 2)
            reward_msgs.append('참가상: 애정도 +2')
        msgs = self._minigame_claim('feed', tier, extra_msgs = reward_msgs)
        self.save_state()
        self._refresh_minigame_hub()
        self._show_minigame_result_popup(win, False, result_lines + msgs, close_fn = _on_close)

    None()
