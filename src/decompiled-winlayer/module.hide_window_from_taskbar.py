# module.hide_window_from_taskbar
# source line 245
# Recovered from bytecode; default argument values are not shown.

def hide_window_from_taskbar(hwnd):
    if not IS_WINDOWS:
        return False

    try:
        hwnd = int(hwnd)
        if not hwnd:
            return False
        if not None(user32, 'GetWindowLongPtrW', None):
        
            try:
                None(user32, 'GetWindowLongPtrW', None)
                get_style = user32.GetWindowLongW
                if not getattr(user32, 'SetWindowLongPtrW', None):
                
                    try:
                        getattr(user32, 'SetWindowLongPtrW', None)
                        set_style = user32.SetWindowLongW
                        cur = None(hwnd, GWL_EXSTYLE)
                        new_style = (cur | WS_EX_TOOLWINDOW) & ~WS_EX_APPWINDOW
                        None(hwnd, GWL_EXSTYLE, new_style)
                        user32.SetWindowPos(hwnd, None, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE | SWP_NOZORDER | SWP_NOACTIVATE | SWP_FRAMECHANGED)
                        return True
                    except Exception:
                        return False
