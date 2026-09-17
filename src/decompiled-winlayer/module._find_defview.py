# module._find_defview
# source line 423
# Recovered from bytecode; default argument values are not shown.

def _find_defview():
    try:
        progman = user32.FindWindowW('Progman', None)
        defview = user32.FindWindowExW(progman, None, 'SHELLDLL_DefView', None)
        if defview:
        
            try:
                listview = user32.FindWindowExW(defview, None, 'SysListView32', None)
                if listview:
                
                    try:
                        return listview
                    
                        try:
                            result = {
                                'hwnd': None }
                            _cb = (lambda hwnd, lparam: try:
    defview2 = user32.FindWindowExW(hwnd, None, 'SHELLDLL_DefView', None)if defview2:
    try:
    listview2 = user32.FindWindowExW(defview2, None, 'SysListView32', None)if listview2:
    try:
    result['hwnd'] = listview2FalseTrueexcept Exception:
    True)()
                            user32.EnumWindows(_cb, 0)
                            return result['hwnd']
                        except Exception:
                            return None
