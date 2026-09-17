# module.PetApp._show_rocket_toast
# source line 13969
# Recovered from bytecode; default argument values are not shown.

def _show_rocket_toast(self):
    if self.state.get('rocket_ambush_location') == 'off':
        return None

    try:
        old = getattr(self, '_rocket_toast_win', None)
        if old is not None and old.winfo_exists():
        
            try:
                old.destroy()
                win = None(self.root)
                self._rocket_toast_win = win
            
                try:
                    win.overrideredirect(True)
                
                    try:
                        win.attributes('-topmost', True)
                        color_mode = self.state.get('rocket_popup_color_mode', 'black')
                        if color_mode == 'color':
                            bg = ()
                            border = ('#111111', '#e02020', '#ff4040', '#dddddd')
                            title_fg = tk.Toplevel
                            sub_fg = None
                        else:
                            bg = ()
                            border = ('#f2f2f2', '#333333', '#000000', '#444444')
                            title_fg = tk.Toplevel
                            sub_fg = None
                        frame.pack(fill = 'both', expand = True)
                    
                        try:
                            None(logo_img) = ImageTk.PhotoImage
                            logo_lbl = None(frame, image = logo_photo, bg = bg)
                            logo_lbl.image = logo_photo
                            logo_lbl.pack(side = 'left', padx = (10, 4), pady = 8)
                            clickable.append(logo_lbl)
                            r_badge = None(frame, text = 'R', font = ('맑은 고딕', 14, 'bold'), fg = '#ffffff', bg = border, width = 2)
                            r_badge.pack(side = 'left', padx = (0, 8), pady = 8)
                            clickable.append(r_badge)
                            text_frame = None(frame, bg = bg)
                            text_frame.pack(side = 'left', fill = 'both', expand = True, pady = 8)
                            title_lbl = None(text_frame, text = '🚀 로켓단 습격!', font = ('맑은 고딕', 12, 'bold'), fg = title_fg, bg = bg, wraplength = 190, justify = 'left', anchor = 'w')
                            title_lbl.pack(anchor = 'w', fill = 'x', pady = (4, 0))
                            sub_lbl = None(text_frame, text = '클릭하면 바로 전투 시작!', font = ('맑은 고딕', 8), fg = sub_fg, bg = bg, wraplength = 190, justify = 'left', anchor = 'w')
                            sub_lbl.pack(anchor = 'w', fill = 'x')
                            clickable.extend([
                                text_frame,
                                title_lbl,
                                sub_lbl])
                            self._toast_corner_geometry(win)
                        
                            def _dismiss():
                                '''_rocket_toast_win'''
                            
                                try:
                                    if getattr(self, '_rocket_toast_win', None) is win:
                                        self._rocket_toast_win = None
                                    win.destroy()
                                    return None
                                except Exception:
                                    return None


                        
                            def _on_click(_evt = None):
                                None()
                                self._start_rocket_ambush()

                            for w_ in clickable:
                                w_.bind('<Button-1>', _on_click)
                            tk.Label
                            _dur = self._toast_duration_ms()
                            if _dur > 0:
                                win.after(_dur, _dismiss)
                                return None
                            return tk.Label
                            except Exception:
                                tk.Label
                                continue
                            except Exception:
                                tk.Label
                                continue
                            except Exception:
                                tk.Label
                                continue
                        except Exception:
                            None(win, bg = bg, highlightbackground = border, highlightthickness = 2)
                            continue
                            except Exception:
                                tk.Frame
                                continue
