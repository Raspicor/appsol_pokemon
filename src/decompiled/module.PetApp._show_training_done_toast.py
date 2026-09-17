# module.PetApp._show_training_done_toast
# source line 9536
# Recovered from bytecode; default argument values are not shown.

def _show_training_done_toast(self):
    if self.state.get('rocket_ambush_location') == 'off':
        return None

    try:
        old = getattr(self, '_train_done_toast_win', None)
        if old is not None and old.winfo_exists():
        
            try:
                old.destroy()
            
                try:
                    win = None(self.root)
                    win.overrideredirect(True)
                    win.attributes('-topmost', True)
                    self._train_done_toast_win = win
                    frame = None(win, bg = '#f2f2f2', relief = 'solid', bd = 1)
                    frame.pack(fill = 'both', expand = True)
                    None(frame, text = '🏋 수련의 방 완료! 눌러서 보상 받기', font = ('맑은 고딕', 9, 'bold'), bg = '#f2f2f2', fg = '#000000', wraplength = 210, justify = 'left').pack(padx = 10, pady = (8, 4))
                
                    def _dismiss():
                        '''_train_done_toast_win'''
                        w = getattr(self, '_train_done_toast_win', None)
                        if w is not None:
                            self._train_done_toast_win = None
                        
                            try:
                                w.destroy()
                                return None
                                return None
                            except Exception:
                                return None


                
                    def _open(_evt = None):
                        None()
                        self.open_training_room()

                    None(frame, text = '🎁 보러가기', font = ('맑은 고딕', 9, 'bold'), bg = '#ffd54a', command = _open).pack(padx = 10, pady = (0, 8))
                    self._toast_corner_geometry(win)
                    _dur = self._toast_duration_ms()
                    if _dur > 0:
                        win.after(_dur, _dismiss)
                        return None
                    return tk.Button
                    except Exception:
                        tk.Frame
                        continue
                except Exception:
                    return None
