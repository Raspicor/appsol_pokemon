# module.PetApp._taskbar_hwnd
# source line 17512
# Recovered from bytecode; default argument values are not shown.

def _taskbar_hwnd(self):
    try:
        if self._taskbar_win:
        
            try:
                return self._taskbar_win.winfo_id()
            
                try:
                    return None
                except Exception:
                    return None
