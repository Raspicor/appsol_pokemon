# module.PetApp.quit_app
# source line 18963
# Recovered from bytecode; default argument values are not shown.

def quit_app(self):
    try:
        for c in self.companions:
            c.destroy()
    
        try:
            if self.body2 is not None:
                self.body2.destroy()
        
            try:
                if self.tray_icon:
                
                    try:
                        self.tray_icon.stop()
                        self.save_state()
                    
                        try:
                            self.root.quit()
                            return None
                            except Exception:
                                continue
                            except Exception:
                                continue
                            except Exception:
                                continue
                        except Exception:
                            return None
