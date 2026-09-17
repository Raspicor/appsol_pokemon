# module.PetApp.open_mining
# source line 11967
# Recovered from bytecode; default argument values are not shown.

def open_mining(self):
    self._migrate_coin_wallet_to_gold()
    if self._mine_run is not None:
    
        try:
            if self._mine_run.winfo_exists():
            
                try:
                    self._mine_run.lift()
                    self._mine_run.focus_force()
                    return None
                    self._mine_run = None
                    if self._mine_today_count() >= MINE_MAX_PER_DAY:
                        None('PikaPet', f'''오늘 광산은 다 다녀왔어요! (하루 {MINE_MAX_PER_DAY}번)\n내일 다시 와주세요.''')
                        return None
                    win = None(self.root)
                    win.title('⛏ 광산')
                    resolve_species_win(win, 380, 300)
                    self._mine_run = win
                    body = None(win)
                    body.pack(fill = 'both', expand = True, padx = 14, pady = 12)
                    None(body, text = '⛏ 광산', font = ('맑은 고딕', 13, 'bold')).pack(pady = (0, 4))
                    None(body, text = '→ 를 꾹 누르고 있으면 주우욱 걸어가요! (톡 치면 아주 살짝만 나가요)\n손을 떼면 그 자리에서 멈춰요. Ctrl을 같이 누르면 2배 빨라져요.', font = ('맑은 고딕', 8), fg = '#666', justify = 'center', wraplength = 340).pack(pady = (0, 6))
                    TRACK_X0, TRACK_X1, TRACK_Y = 30, 320, 60
                    canvas = None(body, width = 350, height = 100, bg = '#eaf4ff', highlightthickness = 1, highlightbackground = '#bbb')
                    canvas.pack(pady = (0, 8))
                    canvas.create_line(TRACK_X0, TRACK_Y, TRACK_X1, TRACK_Y, fill = '#999', width = 3, dash = (4, 2))
                    canvas.create_text(TRACK_X0, TRACK_Y - 32, text = '🏠', font = ('맑은 고딕', 20))
                    canvas.create_text(TRACK_X1, TRACK_Y - 32, text = '⛏', font = ('맑은 고딕', 20))
                    frames_right = ()
                    frames_left = self._mine_marker_frames(40)
                    None(value = '→ 를 눌러서 출발하세요!') = tk.StringVar
                    None(body, textvariable = status_var, font = ('맑은 고딕', 10, 'bold'), fg = '#333').pack(pady = (0, 4))
                    progress_var = None(value = '진행률: 0%')
                    None(body, textvariable = progress_var, font = ('맑은 고딕', 8), fg = '#888').pack()
                    run = {
                        'frame_durations': frame_durations,
                        'frames_left': frames_left,
                        'frames_right': frames_right,
                        'frame_elapsed': 0,
                        'frame_idx': 0,
                        'closed': False,
                        'reward': None,
                        'tick_job': None,
                        'held': {
                            'ctrl': False,
                            'right': False,
                            'left': False },
                        'phase': 'go',
                        'progress': 0 }
                
                    def _advance_walk_anim(dt_ms, moving):
                        if not moving:
                            run['frame_idx'] = 0
                            run['frame_elapsed'] = 0
                            return None
                        durs = None['frame_durations']
                        n = len(durs)
                        0 = None
                        if guard < 10:
                            if run['frame_elapsed'] >= durs[run['frame_idx'] % n]:
                                (run['frame_idx'] + 1) % n = None
                                guard += 1
                                continue
                            return None

                
                    def _total_progress_pct():
                        '''왕복 전체 기준 진행률(0~100%). 갈 때는 0~50%, 도착하면 50%, 돌아올
    때는 50~100%로 이어져서 채워지게 - 예전엔 갈 때 0~100%를 다 채웠다가
    돌아올 때 다시 100%에서 0%로 거꾸로 줄어드는 것처럼 보였다.'''
                        phase = run['phase']
                        if phase == 'go':
                            return run['progress'] * 50
                        if None == 'arrived':
                            return 50
                        if None in ('return', 'returning'):
                            return 50 + (1 - run['progress']) * 50
                        if None == 'done':
                            return 100
                        return None['progress'] * 50

                
                    def _redraw():
                        '''progress'''
                        x = TRACK_X0 + (TRACK_X1 - TRACK_X0) * run['progress']
                    
                        try:
                            frames = run['frames_left'] if run['phase'] in ('return', 'returning') else run['frames_right']
                            idx = run['frame_idx'] % len(frames)
                            canvas.coords(marker_id, x, TRACK_Y)
                            canvas.itemconfig(marker_id, image = frames[idx])
                            None(f'''{_total_progress_pct(None())}%''')
                            return None
                        except Exception:
                            continue


                
                    def _arrive():
                        '''arrived'''
                        run['phase'] = 'arrived'
                        status_var.set('🎉 도착! 코인을 캐는 중... (얼마인지는 돌아가면 알 수 있어요)')
                        None()
                    
                        def _reveal_coin():
                            '''closed'''
                            if run['closed']:
                                return None
                            run['reward'] = None._roll_mine_reward()
                            run['phase'] = 'return'
                            status_var.set('🎒 뭔가 챙겼어요! ← 를 눌러서 돌아오세요!')
                            None()

                        win.after(700, _reveal_coin)

                
                    def _return_home():
                        '''returning'''
                        run['phase'] = 'returning'
                        status_var.set('두구두구...')
                        steps = {
                            'n': 0 }
                    
                        def _drumroll():
                            '''closed'''
                            if run['closed']:
                                return None
                            status_var.set('두구두구' + '.' * (steps['n'] % 4))
                            if steps['n'] < 5:
                                win.after(280, _drumroll)
                                return None
                            if not None['reward']:
                                None['reward']
                            0 = None
                            self._earn_gold(reward, source = 'mine')
                            self._mine_bump_today()
                            self.save_state()
                            run['phase'] = 'done'
                            status_var.set(f'''💰 얼마 벌어왔어요! +{reward}골드! (오늘 {self._mine_today_count()}/{MINE_MAX_PER_DAY}회 사용)''')
                            None()

                        win.after(280, _drumroll)

                
                    def _restart_run():
                        run['progress'] = 0
                        run['phase'] = 'go'
                        run['reward'] = None
                        run['frame_idx'] = 0
                        run['frame_elapsed'] = 0
                        status_var.set('→ 를 눌러서 출발하세요!')
                    
                        try:
                            replay_btn.pack_forget()
                        
                            try:
                                close_btn.pack_forget()
                                None()
                                None()
                                return None
                                except Exception:
                                    _redraw
                                    continue
                            except Exception:
                                continue



                
                    def _offer_replay_or_close():
                        remaining = MINE_MAX_PER_DAY - self._mine_today_count()
                        if remaining > 0:
                        
                            try:
                                replay_btn.configure(text = f'''▶ 한 번 더 하기 (오늘 {remaining}회 남음)''')
                                replay_btn.pack(pady = (6, 0))
                                return None
                            
                                try:
                                    close_btn.configure(text = '닫기')
                                    close_btn.pack(pady = (6, 0))
                                    return None
                                    except Exception:
                                        return None
                                except Exception:
                                    return None



                
                    def _apply_tap_nudge(which):
                        '''held'''
                        step = MINE_TAP_STEP * MINE_SECRET_SPEED_MULT if run['held']['ctrl'] else 1
                        if which == 'right' and run['phase'] == 'go':
                            run['progress'] = min(1, run['progress'] + step)
                            None()
                            if run['progress'] >= 1:
                                None()
                                return None
                            return _redraw
                        if None == 'left':
                            if run['phase'] == 'return':
                                run['progress'] = max(0, run['progress'] - step)
                                None()
                                if run['progress'] <= 0:
                                    None()
                                    return None
                                return _redraw
                            return None

                
                    def _tick():
                        '''closed'''
                        if not run['closed'] or win.winfo_exists():
                            return None
                        None()
                        dt = 0.05
                        speed = 1 / MINE_TRIP_SECONDS
                        if run['held']['ctrl']:
                            speed *= MINE_SECRET_SPEED_MULT
                        moving = False
                        arrived_now = False
                        returned_now = False
                        if run['phase'] == 'go' and run['held']['right']:
                            moving = True
                            run['progress'] = min(1, run['progress'] + speed * dt)
                            if run['progress'] >= 1:
                                arrived_now = True
                            elif run['phase'] == 'return' and run['held']['left']:
                                moving = True
                                run['progress'] = max(0, run['progress'] - speed * dt)
                                if run['progress'] <= 0:
                                    returned_now = True
                        None(50, moving)
                        None()
                        if arrived_now:
                            None()
                        elif returned_now:
                            None()
                        run['tick_job'] = win.after(50, _tick)

                
                    def _key_press(which):
                    
                        def _h(evt = None):
                            '''held'''
                            was_held = run['held'].get(which, False)
                            run['held'][which] = True
                            if not which in ('right', 'left') and was_held:
                                None(which)
                            if which == 'right' and run['phase'] == 'go':
                                status_var.set('→ 이동 중...')
                                return None
                            if _apply_tap_nudge == 'left':
                                if run['phase'] == 'return':
                                    status_var.set('← 복귀 중...')
                                    return None
                                return None

                        return _h

                
                    def _key_release(which):
                    
                        def _h(evt = None):
                            run['held'][which] = False
                            if which == 'right' and run['phase'] == 'go' and run['progress'] < 1:
                                status_var.set('멈췄어요. → 를 다시 눌러서 이동하세요!')
                                return None
                            if None == 'left':
                                if run['phase'] == 'return':
                                    if run['progress'] > 0:
                                        status_var.set('멈췄어요(뭔가 챙긴 채). ← 를 다시 눌러서 이동하세요!')
                                        return None
                                    return None
                                return None

                        return _h

                    '<KeyPress-Right>'(_key_press, None('right'))
                    '<KeyRelease-Right>'(_key_release, None('right'))
                    '<KeyPress-Left>'(_key_press, None('left'))
                    '<KeyRelease-Left>'(_key_release, None('left'))
                    '<KeyPress-Control_L>'(_key_press, None('ctrl'))
                    '<KeyRelease-Control_L>'(_key_release, None('ctrl'))
                    '<KeyPress-Control_R>'(_key_press, None('ctrl'))
                    '<KeyRelease-Control_R>'(_key_release, None('ctrl'))
                
                    def _grab_focus():
                    
                        try:
                            win.lift()
                            win.focus_force()
                            return None
                        except Exception:
                            return None


                    None()
                    win.after(60, _grab_focus)
                    win.after(300, _grab_focus)
                    win.bind('<Button-1>', (lambda e: win.after(10, _grab_focus)))
                
                    try:
                        win.grab_set()
                    
                        def _on_close():
                            run['closed'] = True
                            if run['tick_job']:
                            
                                try:
                                    win.after_cancel(run['tick_job'])
                                    self._mine_run = None
                                
                                    try:
                                        win.grab_release()
                                        win.destroy()
                                        return None
                                        except Exception:
                                            continue
                                    except Exception:
                                        continue



                        win.protocol('WM_DELETE_WINDOW', _on_close)
                        replay_btn = None(body, text = '▶ 한 번 더 하기', command = _restart_run, takefocus = 0)
                        close_btn = None(body, text = '닫기', command = _on_close, takefocus = 0)
                        self._add_opacity_control(win)
                        None()
                        return None
                        except Exception:
                            tk.Button
                            continue
                    except Exception:
                        win.bind
                        continue
