# module.get_window_ledges
# source line 366
# Recovered from bytecode; default argument values are not shown.

def get_window_ledges(exclude_titles, max_windows):
    if not IS_WINDOWS:
        return []
    if not None:
        pass
    exclude_titles = []
    ledges = []

    try:
        _cb = (lambda hwnd, lparam: try:
    if len(ledges) >= max_windows:
    Trueif not None.IsWindowVisible(hwnd):
    Trueif None.IsIconic(hwnd):
    Truelength = None.GetWindowTextLengthW(hwnd)if length <= 0:
    Truebuf = None(length + 1)user32.GetWindowTextW(hwnd, buf, length + 1)title = buf.valueif not title:
    Trueif None.create_unicode_buffer is <common_constant>:
    try:
    None.create_unicode_bufferfor None in exclude_titles():
    if not None:
    continuetry:
    exclude_titles()if False:
    Truerect = None.RECT()if not hwnd(ctypes.byref, None(rect)):
    Truewidth = user32.GetWindowRect.right - rect.leftheight = rect.bottom - rect.topif width < 80 or height < 40:
    TrueNone.append({
    'title': title,
    'right': rect.right,
    'top': rect.top,
    'left': rect.left })Trueexcept Exception:
    (lambda .0: for None in .0:
    t = Noneif t:
    tt in title)
                                return True


    )()
        user32.EnumWindows(_cb, 0)
        return ledges
    except Exception:
        return 
