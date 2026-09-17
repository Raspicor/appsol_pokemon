# module.PetApp._show_todo_alarm_toast
# source line 9505
# Recovered from bytecode; default argument values are not shown.

def _show_todo_alarm_toast(self, todo_item):
    try:
        win = None(self.root)
        win.overrideredirect(True)
        win.attributes('-topmost', True)
        frame = None(win, bg = '#fff3cd', relief = 'solid', bd = 1)
        frame.pack(fill = 'both', expand = True)
        None(frame, text = f'''⏰ 알람 시간이에요!\n{todo_item.get('text', '')}''', font = ('맑은 고딕', 9, 'bold'), bg = '#fff3cd', fg = '#000000', wraplength = 210, justify = 'left').pack(padx = 10, pady = (8, 4))
    
        def _dismiss():
        
            try:
                win.destroy()
                return None
            except Exception:
                return None


        None(frame, text = '확인', font = ('맑은 고딕', 9, 'bold'), bg = '#ffd54a', command = _dismiss).pack(padx = 10, pady = (0, 8))
        self._toast_corner_geometry(win)
    
        try:
            dur = float(todo_item.get('popup_dur', 5))
            if dur > 0:
                win.after(int(dur * 1000), _dismiss)
                return None
            return tk.Button
            except Exception:
                tk.Frame
                return None
        except Exception:
            tk.Label
            dur = 5
            continue
