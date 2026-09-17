# module.PetApp.open_todo
# source line 18531
# Recovered from bytecode; default argument values are not shown.

def open_todo(self):
    win = None(self.root)
    win.title('할일 / 시계')
    resolve_species_win(win, 340, 560)

    try:
        win.geometry('340x560')
        win.minsize(300, 360)
        win.resizable(True, True)
        bottom = None(win)
        bottom.pack(side = 'bottom', pady = 10)
        top_area = None(win)
        top_area.pack(side = 'top', fill = 'both', expand = True)
        clock_var = time.strftime(value = None('%Y-%m-%d %H:%M:%S'))
        None(top_area, textvariable = clock_var, font = ('맑은 고딕', 11)).pack(pady = (10, 6))
    
        def _tick_clock():
            if not win.winfo_exists():
                return None
            time.strftime(None('%Y-%m-%d %H:%M:%S'))
            win.after(1000, _tick_clock)

        win.after(1000, _tick_clock)
        entry_row = None(top_area)
        entry_row.pack(fill = 'x', padx = 10, pady = (0, 4))
        entry = None(entry_row, width = 24)
        entry.pack(side = 'left', fill = 'x', expand = True)
        alarm_on_var = None(value = False)
        alarm_row = None(top_area)
        alarm_row.pack(fill = 'x', padx = 10, pady = (0, 4))
        None(alarm_row, text = '⏰ 알람 시간 정하기', variable = alarm_on_var).pack(side = 'left')
        alarm_detail_row = None(top_area)
        hour_var = time.strftime(value = None('%H'))
        min_var = time.strftime(value = None('%M'))
        None(alarm_detail_row, text = '시각:', font = ('맑은 고딕', 8)).pack(side = 'left', padx = (10, 2))
        None(alarm_detail_row, textvariable = hour_var, from_ = 0, to = 23, width = 3, format = '%02.0f', wrap = True).pack(side = 'left')
        None(alarm_detail_row, text = ':', font = ('맑은 고딕', 8)).pack(side = 'left')
        None(alarm_detail_row, textvariable = min_var, from_ = 0, to = 59, width = 3, format = '%02.0f', wrap = True).pack(side = 'left')
        None(alarm_detail_row, text = '(지난 시각이면 내일로 자동 예약)', font = ('맑은 고딕', 7), fg = '#888').pack(side = 'left', padx = (6, 0))
        dur_row = None(top_area)
        None(dur_row, text = '알람 팝업 유지시간:', font = ('맑은 고딕', 8)).pack(side = 'left', padx = (10, 4))
        dur_var = None(value = 5)
        for None in (('3초', 3), ('5초', 5), ('10초', 10), ('안사라짐', 0)):
            label = ()
            secs = None
        (('3초', 3), ('5초', 5), ('10초', 10), ('안사라짐', 0))
        alarm_on_var.trace_add('write', _toggle_alarm_ui)
        None(top_area) = tk.Frame
        list_outer.pack(fill = 'both', expand = True, padx = 10, pady = (6, 4))
        list_canvas = None(list_outer, highlightthickness = 0)
        list_vsb = None(list_outer, orient = 'vertical', command = list_canvas.yview)
        list_inner = None(list_canvas)
        _list_win_id = list_canvas.create_window((0, 0), window = list_inner, anchor = 'nw')
        list_inner.bind('<Configure>', (lambda e: list_canvas.configure(scrollregion = list_canvas.bbox('all'))))
        list_canvas.bind('<Configure>', (lambda e: list_canvas.itemconfig(_list_win_id, width = e.width)))
        list_canvas.configure(yscrollcommand = list_vsb.set)
        list_canvas.pack(side = 'left', fill = 'both', expand = True)
        list_vsb.pack(side = 'right', fill = 'y')
    
        def _list_wheel(event):
            '''num'''
            delta = -1 if getattr(event, 'num', 0) == 5 or event.delta < 0 else 1
        
            try:
                if list_canvas.winfo_exists():
                
                    try:
                        list_canvas.yview_scroll(-delta, 'units')
                        return None
                        return None
                    except Exception:
                        return None



        win.bind('<MouseWheel>', _list_wheel)
        win.bind('<Button-4>', _list_wheel)
        win.bind('<Button-5>', _list_wheel)
    
        def _add():
            val = entry.get().strip()
            if not val:
                return None
            item = {
                'popup_dur': 5,
                'alarm_fired': False,
                'alarm_at': None,
                'done': False,
                **val }
            if alarm_on_var.get():
            
                try:
                    hh = int(hour_var.get())
                    mm = int(min_var.get())
                    now_t = None()
                    target = None((now_t.tm_year, now_t.tm_mon, now_t.tm_mday, hh, mm, 0, 0, 0, -1))
                    if time.time <= None():
                        target += 86400
                    item['alarm_at'] = target
                    item['popup_dur'] = dur_var.get()
                    self._todo_list().append(item)
                    self.save_state()
                    entry.delete(0, 'end')
                    alarm_on_var.set(False)
                    None()
                    return None
                except Exception:
                    mm = 0
                    hh = 0
                    continue


    
        def _toggle_done(item):
            '''done'''
            item['done'] = not item.get('done', False)
            self.save_state()
            None()

    
        def _delete_item(item):
            todos = self._todo_list()
        
            try:
                todos.remove(item)
                self.save_state()
                None()
                return None
            except ValueError:
                continue


    
        def _render_list():
            '''done'''
            for w in list_inner.winfo_children():
                w.destroy()
            todos = self._todo_list()
            for None in :
                t = None
                if t.get('done'):
                    continue
        
            , [], pending, t = todos, t
            for None in :
                t = None
                if not t.get('done'):
                    continue
        
            , [], done, t = todos, t
        
            def _row(parent, t):
                '''groove'''
                row = None(parent, relief = 'groove', bd = 1, padx = 4, pady = 3)
                row.pack(fill = 'x', pady = 2)
                chk_var = None(value = bool(t.get('done')))
                None(row, variable = chk_var, command = (lambda : None(t))).pack(side = 'left')
                alarm_txt = ''
                if t.get('alarm_at'):
                    alarm_txt = time.strftime + '%m/%d %H:%M'(time.localtime, None(t['alarm_at']))
                    if t.get('alarm_fired'):
                        alarm_txt += '(알림됨)'
                text_disp = t.get('text', '')
                if t.get('done'):
                    text_disp = '✅ ' + text_disp
                None(row, text = text_disp + alarm_txt, font = ('맑은 고딕', 9), wraplength = 190, justify = 'left', anchor = 'w').pack(side = 'left', fill = 'x', expand = True, padx = (4, 4))
                None(row, text = '삭제', font = ('맑은 고딕', 7), command = (lambda : None(t))).pack(side = 'right')

            if not pending and done:
                None(list_inner, text = '할일이 없어요. 위에서 추가해보세요!', font = ('맑은 고딕', 8), fg = '#888').pack(pady = 10)
                return None
            None(list_inner, text = f'''◽ 미완료 ({len(pending)})''', font = ('맑은 고딕', 8, 'bold'), fg = '#1a4a8a').pack(anchor = 'w', pady = (2, 0))
            if not pending:
                None(list_inner, text = '(없음)', font = ('맑은 고딕', 8), fg = '#aaa').pack(anchor = 'w')
            for t in pending:
                None(list_inner, t)
            pending
            None(list_inner, text = f'''✅ 완료 ({len(done)})''', font = ('맑은 고딕', 8, 'bold'), fg = '#1a6b1a').pack(anchor = 'w', pady = (8, 0))
            if not done:
                None(list_inner, text = '(없음)', font = ('맑은 고딕', 8), fg = '#aaa').pack(anchor = 'w')
            for t in done:
                None(list_inner, t)
            done
            return None
        
        

        btn_row = None(top_area)
        btn_row.pack(pady = (0, 4))
        None(btn_row, text = '➕ 추가', command = _add).pack(side = 'left', padx = 4)
        None()
        None(bottom, text = '닫기', command = win.destroy).pack()
        self._add_opacity_control(win)
        return None
    except Exception:
        continue
