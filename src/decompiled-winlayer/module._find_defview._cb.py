# module._find_defview._cb
# source line 435
# Recovered from bytecode; default argument values are not shown.

def _cb(hwnd, lparam):
    try:
        defview2 = user32.FindWindowExW(hwnd, None, 'SHELLDLL_DefView', None)
        if defview2:
        
            try:
                listview2 = user32.FindWindowExW(defview2, None, 'SysListView32', None)
                if listview2:
                
                    try:
                        result['hwnd'] = listview2
                        return False
                        return True
                    except Exception:
                        return True
