# module.PetApp._compute_screen_rect
# source line 4934
# Recovered from bytecode; default argument values are not shown.

def _compute_screen_rect(self):
    if self.state.get('secondary_monitor_mode'):
    
        try:
            rect = None()
            if rect:
                return rect
            if winlayer.get_secondary_monitor_rect.state.get('single_monitor_mode') or self.state.get('secondary_monitor_mode'):
            
                try:
                    w = self.root.winfo_screenwidth()
                    h = self.root.winfo_screenheight()
                    return (0, 0, max(1, w), max(1, h))
                
                    try:
                        vrect = None()
                        if vrect:
                            return vrect
                    
                        try:
                            w = self.root.winfo_screenwidth()
                            h = self.root.winfo_screenheight()
                            return (0, 0, max(1, w), max(1, h))
                            except Exception:
                                rect = None
                                continue
                            except Exception:
                                h = 720
                                w = 1280
                                continue
                            except Exception:
                                vrect = None
                                continue
                        except Exception:
                            h = 720
                            w = 1280
                            continue
