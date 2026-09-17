# module.PetApp.open_mining._on_close
# source line 12239
# Recovered from bytecode; default argument values are not shown.

def _on_close():
    run['closed'] = True
    if run['tick_job']:
    
        try:
            win.after_cancel(run['tick_job'])
            self._mine_run = None
        
            try:
                win.grab_release()
                win.destroy()
                return None
                except Exception:
                    continue
            except Exception:
                continue
