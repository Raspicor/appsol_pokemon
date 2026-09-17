# module.PetApp._rocket_screen_rect
# source line 4967
# Recovered from bytecode; default argument values are not shown.

def _rocket_screen_rect(self):
    loc = self.state.get('rocket_ambush_location', 'any')
    if loc == 'main':
    
        try:
            w = self.root.winfo_screenwidth()
            h = self.root.winfo_screenheight()
            return (0, 0, max(1, w), max(1, h))
            if loc == 'secondary':
            
                try:
                    rect = None()
                    if rect:
                        return rect
                    return (winlayer.get_secondary_monitor_rect.screen_left, self.screen_top, self.screen_w, self.screen_h)
                    except Exception:
                        continue
                except Exception:
                    rect = None
                    continue
