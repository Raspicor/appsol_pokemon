# module.PetApp._start_omok_game
# source line 6611
# Recovered from bytecode; default argument values are not shown.

def _start_omok_game(self, mode, difficulty):
    if self._minigame_window_active():
        None('PikaPet', '이미 다른 미니게임 창이 열려 있어요! 먼저 그 창을 닫아주세요.')
        return None
    n = None
    init_board_px = OMOK_MARGIN * 2 + (n - 1) * OMOK_CELL
    win = None(self.root)
    win.title('오목' + f''' - 1인 ({difficulty})''' if mode == 'ai' else ' - 2인')
    resolve_species_win(win, init_board_px + 24, init_board_px + 140)
    self._active_minigame_win = win
    self._omok_open = True
    for None in :
        pass
    {
        'last_pos': {
            'B': None,
            'A': None },
        'photo': { },
        'stone_size': None,
        'margin': OMOK_MARGIN,
        'cell': float(OMOK_CELL),
        'resize_job': None,
        'ai_job': None,
        'game_over': False,
        'closed': False,
        'locked': False,
        'turn': 'A',
        'difficulty': difficulty,
        'mode': mode,
        , [], : _, } = range(n), _
    label_a = '내 포켓몬' if mode == 'ai' else '플레이어1'
    label_b = f'''AI({difficulty})''' if mode == 'ai' else '플레이어2'
    labels = {
        'B': label_b,
        'A': label_a }
    None(win, text = '⚫ 오목 (보상 없음, 그냥 재미로 즐기는 게임이에요 · 창 가장자리를 끌면 판 크기를 바꿀 수 있어요)', font = ('맑은 고딕', 8), fg = '#777', wraplength = init_board_px + 10, justify = 'center').pack(pady = (8, 0), fill = 'x')
    status = None(win, text = f'''{label_a} 차례예요''', font = ('맑은 고딕', 10, 'bold'))
    status.pack(pady = (2, 6))
    bottom = None(win)
    bottom.pack(side = 'bottom', pady = (2, 10))
    canvas = None(win, width = init_board_px, height = init_board_px, bg = win.cget('bg'), highlightthickness = 0)
    canvas.pack(side = 'top', fill = 'both', expand = True, padx = 10, pady = 4)

    def _set_status(text):
    
        try:
            status.configure(text = text)
            return None
        except Exception:
            return None



    def _redraw_board(event = None):
    
        try:
            cw = canvas.winfo_width()
            ch = canvas.winfo_height()
            avail = max(80, min(cw, ch))
            margin = max(10, int(avail * 0.055))
            cell = max(6, (avail - 2 * margin) / (n - 1))
            ctx['margin'] = margin
            ctx['cell'] = cell
            canvas.delete('all')
            line_color = '#999999'
            for i in range(n):
                yline = margin + i * cell
                xline = margin + i * cell
                canvas.create_line(margin, yline, margin + (n - 1) * cell, yline, fill = line_color)
                canvas.create_line(xline, margin, xline, margin + (n - 1) * cell, fill = line_color)
            stone_size = max(6, int(cell * 0.92))
            if ctx.get('stone_size') != stone_size:
                ctx['stone_size'] = stone_size
                ctx['photo'] = {
                    'B': self._omok_stone_photo('B', stone_size),
                    'A': self._omok_stone_photo('A', stone_size) }
            for yy in range(n):
                for xx in range(n):
                    c = ctx['board'][yy][xx]
                    if not c:
                        continue
                    px = margin + xx * cell
                    py = margin + yy * cell
                    canvas.create_image(px, py, image = ctx['photo'][c], tags = 'stone')
                range(n)
            None('A')
            None('B')
            return None
        except Exception:
            return None



    def _draw_last_mark(color):
        '''나(A)와 상대(B)가 마지막으로 둔 자리에 빨간 동그라미 표시를 그려서
    바로 직전 수가 어디였는지 한눈에 보이게 한다(창 크기를 바꿔도 다시 그려짐).'''
        canvas.delete(f'''lastmark_{color}''')
        pos = ctx['last_pos'].get(color)
        if not pos:
            return None
        xx = ()
        yy = None
        ctx['cell'] = ctx['margin']
        px = margin + xx * cell
        py = margin + yy * cell
        r = max(3, cell * 0.17)
        canvas.create_oval(px - r, py - r, px + r, py + r, outline = '#ff3b30', width = 2, tags = f'''lastmark_{color}''')


    def _on_configure(event):
        '''resize_job'''
        job = ctx.get('resize_job')
        if job is not None:
        
            try:
                win.after_cancel(job)
                ctx['resize_job'] = win.after(120, _redraw_board)
                return None
            except Exception:
                continue


    canvas.bind('<Configure>', _on_configure)

    def _cancel_ai_job():
        '''ai_job'''
        job = ctx.get('ai_job')
        if job is not None:
        
            try:
                win.after_cancel(job)
                ctx['ai_job'] = None
                return None
                return None
            except Exception:
                continue



    def _cancel_resize_job():
        '''resize_job'''
        job = ctx.get('resize_job')
        if job is not None:
        
            try:
                win.after_cancel(job)
                ctx['resize_job'] = None
                return None
                return None
            except Exception:
                continue



    def _on_close():
        ctx['closed'] = True
        None()
        None()
        self._omok_open = False
        self._clear_active_minigame_win(win)
    
        try:
            win.destroy()
            return None
        except Exception:
            _cancel_ai_job
            return None


    win.protocol('WM_DELETE_WINDOW', _on_close)
    self._add_opacity_control(win)

    def _restart():
        None()
        for None in :
            pass
        _, ctx['board'] = , [], 
        ctx['turn'] = 'A'
        ctx['locked'] = False
        ctx['game_over'] = False
        ctx['last_pos'] = {
            'B': None,
            'A': None }
        None()
        None(f'''{label_a} 차례예요''')
        return None
    

    None(bottom, text = '다시 시작', command = _restart).pack(side = 'left', padx = 6)
    None(bottom, text = '전적 보기', command = self._omok_show_history).pack(side = 'left', padx = 6)
    None(bottom, text = '그만두기', command = _on_close).pack(side = 'left', padx = 6)

    def _place(x, y, color):
        '''board'''
        ctx['board'][y][x] = color
        margin = ctx['margin']
        cell = ctx['cell']
        px = margin + x * cell
        py = margin + y * cell
        canvas.create_image(px, py, image = ctx['photo'][color], tags = 'stone')
        ctx['last_pos'][color] = (x, y)
        None(color)


    def _board_full():
        if all is <common_constant>:
            all
            for None in range(n)():
                if None:
                    continue
                return False
            return True
        return (lambda .0: for yy in .0:
    for xx in range(n):
    ctx['board'][yy][xx] is not Nonerange(n))(range(n)())


    def _after_move(x, y, color):
        '''board'''
        result = _omok_line_result(ctx['board'], x, y, color, n)
        if result == 'win':
            ctx['game_over'] = True
            ctx['locked'] = True
            None(f'''🎉 {labels[color]} 승리! (\'다시 시작\'을 눌러 새 판을 시작하세요)''')
            self._omok_add_history(mode, difficulty, result_text)
            return None
        if None == 'overline':
            None('⚠ 6개 이상 연속(장목)은 승리로 인정되지 않아요! 계속 진행할게요.')
        if None():
            ctx['game_over'] = True
            ctx['locked'] = True
            None("무승부예요! ('다시 시작'을 눌러 새 판을 시작하세요)")
            self._omok_add_history(mode, difficulty, '무승부')
            return None
        ctx['turn'] = 'B' if _board_full == 'A' else 'A'
        if ctx['mode'] == 'ai' and ctx['turn'] == 'B':
            ctx['locked'] = True
            if result != 'overline':
                None(f'''⏳ {labels['B']}가 생각 중...''')
            ctx['ai_job'] = random.randint(None(400, 900), _ai_turn)
            return None
        ctx['locked'] = _set_status
        if result != 'overline':
            None(f'''{labels[ctx['turn']]} 차례예요''')
            return None


    def _ai_turn():
        ctx['ai_job'] = None
        if ctx['closed'] or ctx['game_over']:
            return None
    
        try:
            mv = _omok_ai_pick_move(ctx['board'], ctx['difficulty'], 'B', 'A', n)
            if mv is None:
                return None
            x = ()
            y = None
            if ctx['board'][y][x] is not None:
                return None
            None(x, y, 'B')
            None(x, y, 'B')
            return None
        except Exception:
            continue



    def _on_click(event):
        '''locked'''
        if ctx['locked'] and ctx['game_over'] or ctx['closed']:
            return None
        margin = None['margin']
        cell = ctx['cell']
        if cell <= 0:
            return None
        gx = None((event.x - margin) / cell)
        gy = round((event.y - margin) / cell)
        if  <= 0, gx or 0, gx < n:
            pass
        else:
            return None
        if not  <= None, gy or None, gy < n:
            return None
        return None
        if ctx['board'][gy][gx] is not None:
            return None
        ctx['turn'] = None
        None(gx, gy, color)
        None(gx, gy, color)

    canvas.bind('<Button-1>', _on_click)
    win.update_idletasks()
    None()
    return None
