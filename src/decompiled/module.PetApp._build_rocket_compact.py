# module.PetApp._build_rocket_compact
# source line 14073
# Recovered from bytecode; default argument values are not shown.

def _build_rocket_compact(self, gctx):
    win = gctx['win']
    for w in win.winfo_children():
        w.destroy()

    try:
        win.overrideredirect(True)
        win.attributes('-topmost', True)
        color_mode = self.state.get('rocket_popup_color_mode', 'black')
        if color_mode == 'color':
            body_bg = ()
            header_bg = ('#241010', '#e02020', 'white', '#ffb0b0')
            header_fg = None
            enemy_fg = None
        else:
            body_bg = ()
            header_bg = ('#1a1a1a', '#1a1a1a', '#ffffff', '#cccccc')
            header_fg = None
            enemy_fg = None
        win.configure(bg = body_bg)
        W, H = 250, 250
        self._position_compact(win, W, H, rect = self._rocket_screen_rect())
        header = None(win, bg = header_bg, cursor = 'fleur')
        header.pack(side = 'top', fill = 'x')
        header_label = None(header, text = '🚀 로켓단 습격! (드래그로 이동)', bg = header_bg, fg = header_fg, font = ('맑은 고딕', 9, 'bold'), cursor = 'fleur')
        header_label.pack(side = 'left', padx = 6, pady = 3)
        None(header, text = '✕', width = 2, command = (lambda : self._gym_concede(gctx))).pack(side = 'right', pady = 2, padx = (0, 3))
        None(header, text = '⟲', width = 2, command = (lambda : self._position_compact(win, W, H, rect = self._rocket_screen_rect()))).pack(side = 'right', pady = 2)
        self._bind_compact_drag(win, header, header_label)
        expand_bar = None(win, bg = body_bg)
        expand_bar.pack(side = 'bottom', fill = 'x', padx = 10, pady = (2, 8))
        None(expand_bar, text = '🔍 화면 키우기 (전투 시작)', command = (lambda : self._expand_rocket_battle(gctx))).pack(fill = 'x')
        None(expand_bar, text = '도망치기', command = (lambda : self._gym_concede(gctx))).pack(fill = 'x', pady = (6, 0))
        canvas_holder = None(win, bg = body_bg)
        canvas_holder.pack(side = 'top', fill = 'both', expand = True, padx = 4)
        canvas = None(canvas_holder, bg = body_bg, highlightthickness = 0)
        vsb = None(canvas_holder, orient = 'vertical', command = canvas.yview)
        body = None(canvas, bg = body_bg, padx = 8, pady = 8)
        body.bind('<Configure>', (lambda e: canvas.configure(scrollregion = canvas.bbox('all'))))
        canvas.create_window((0, 0), window = body, anchor = 'n')
        canvas.configure(yscrollcommand = vsb.set)
        canvas.pack(side = 'left', fill = 'both', expand = True)
        vsb.pack(side = 'right', fill = 'y')
    
        def _wheel(e):
        
            try:
                if e.delta > 0:
                
                    try:
                        pass
                    return None
                    except Exception:
                        return None



        win.bind('<MouseWheel>', _wheel)
    
        try:
            logo_img = load_rocket_logo_image(48)
            self._rocket_compact_logo = None(logo_img)
            None(body, image = self._rocket_compact_logo, bg = body_bg).pack(pady = (2, 6))
            None(body, text = '로켓단이 앞을 가로막았다!', bg = body_bg, fg = '#ffffff', font = ('맑은 고딕', 10, 'bold'), wraplength = 210, justify = 'left').pack(anchor = 'w')
            enemy_names = (lambda .0: for None in .0:
    m = Nonem.get('name', '?'))(gctx['enemy']())
            None(body, text = f'''상대: {enemy_names}''', bg = body_bg, fg = enemy_fg, font = ('맑은 고딕', 9), wraplength = 210, justify = 'left').pack(anchor = 'w', pady = (6, 0))
            None(body, text = f'''내 편성: {len(gctx['player'])}마리''', bg = body_bg, fg = '#cccccc', font = ('맑은 고딕', 9), wraplength = 210, justify = 'left').pack(anchor = 'w', pady = (2, 4))
            gctx['_rocket_compact_active'] = True
            self._schedule_rocket_auto_dismiss(gctx)
            return None
            except Exception:
                tk.Label
                continue
        except Exception:
            tk.Scrollbar
            continue
