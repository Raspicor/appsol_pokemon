# module.PetApp._show_fx_toast
# source line 7293
# Recovered from bytecode; default argument values are not shown.

def _show_fx_toast(self, text, duration, bg):
    try:
        old = getattr(self, '_fx_toast_win', None)
        if old is not None:
            old.destroy()
    
        try:
            win = None(self.root)
            win.overrideredirect(True)
            win.attributes('-topmost', True)
            lbl = None(win, text = text, font = ('맑은 고딕', 12, 'bold'), bg = bg, fg = '#5a3d00', padx = 12, pady = 6, relief = 'solid', bd = 2)
            lbl.pack()
            win.update_idletasks()
            ww = max(1, win.winfo_width())
            wh = max(1, win.winfo_height())
        
            try:
                rx = self.root.winfo_x()
                ry = self.root.winfo_y()
                if not self.root.winfo_width():
                    self.root.winfo_width()
                rw = 1
            
                try:
                    px = rx + rw // 2 - ww // 2
                    py = ry - wh - 8
                    px = max(self.screen_left, min(self.screen_left + self.screen_w - ww, px))
                    py = max(self.screen_top, py)
                    win.geometry(f'''+{int(px)}+{int(py)}''')
                    self._fx_toast_win = win
                    self.root.after(max(500, int(duration * 1000)), (lambda : self._destroy_fx_toast(win)))
                    return None
                    except Exception:
                        tk.Toplevel
                        continue
                    except Exception:
                        tk.Toplevel
                        rw = 1
                        ry = self.screen_top
                        rx = self.screen_left
                    
                        try:
                            continue
                        
                            try:
                                pass
                            except Exception:
                                return None
