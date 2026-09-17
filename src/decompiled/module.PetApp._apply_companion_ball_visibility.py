# module.PetApp._apply_companion_ball_visibility
# source line 7141
# Recovered from bytecode; default argument values are not shown.

def _apply_companion_ball_visibility(self):
    in_ball = self.state.get('in_ball', False)
    for c in self.companions:
        if in_ball:
            c.win.withdraw()
            continue
        c.win.deiconify()
    if getattr(self, 'body2', None) is not None:
    
        try:
            if in_ball:
            
                try:
                    self.body2.win.withdraw()
                    return None
                
                    try:
                        self.body2.win.deiconify()
                        return None
                        return None
                        except Exception:
                            continue
                    except Exception:
                        return None
