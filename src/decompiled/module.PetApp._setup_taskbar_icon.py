# module.PetApp._setup_taskbar_icon
# source line 17458
# Recovered from bytecode; default argument values are not shown.

def _setup_taskbar_icon(self):
    try:
        win = None(self.root)
        win.title('PikaPet')
    
        try:
            self._taskbar_icon_img = None(self._tray_image())
            win.iconphoto(True, self._taskbar_icon_img)
        
            try:
                win.resizable(False, False)
            
                try:
                    win.geometry('1x1+0+0')
                
                    try:
                    
                        def _force_iconify(_evt = None):
                            '''iconic'''
                        
                            try:
                                if win.state() != 'iconic':
                                
                                    try:
                                        win.iconify()
                                        return None
                                        return None
                                    except Exception:
                                        return None



                        win.protocol('WM_DELETE_WINDOW', _force_iconify)
                        win.bind('<Map>', _force_iconify)
                        win.update_idletasks()
                    
                        try:
                            None(win.winfo_id())
                        
                            try:
                                win.iconify()
                                self._taskbar_win = win
                                win.withdraw()
                                return None
                                except Exception:
                                    ImageTk.PhotoImage
                                
                                    try:
                                        continue
                                    
                                        try:
                                            except Exception:
                                                tk.Toplevel
                                            
                                                try:
                                                    continue
                                                
                                                    try:
                                                        except Exception:
                                                        
                                                            try:
                                                                continue
                                                            
                                                                try:
                                                                    pass
                                                                except Exception:
                                                                    self._taskbar_win = None
                                                                    return None
