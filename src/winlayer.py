# Source Generated with Decompyle++
# File: winlayer.pyc (Python 3.14)

'''
winlayer.py
윈도우 창 위에 올라타기 / 바탕화면 아이콘 위치 읽기 용 Win32 ctypes 유틸리티.

주의: 이 파일의 기능들은 실제 Windows 환경에서만 동작하며, 이 프로젝트를
만든 샌드박스에는 Windows/tkinter가 없어 직접 실행 테스트를 하지 못했습니다.
모든 함수는 실패해도 프로그램이 죽지 않도록 try/except로 방어적으로 작성했습니다.
'''
import sys
import ctypes
import struct
IS_WINDOWS = sys.platform.startswith('win')
if IS_WINDOWS:
    import ctypes.wintypes as ctypes
    user32 = ctypes.windll.user32
    kernel32 = ctypes.windll.kernel32
    wintypes = ctypes.wintypes
    user32.EnumWindows.restype = ctypes.c_bool
    user32.EnumWindows.argtypes = [
        None(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM),
        wintypes.LPARAM]
    user32.GetWindowRect.restype = ctypes.c_bool
    user32.GetWindowRect.argtypes = [
        ctypes.POINTER,
        None(wintypes.RECT)]
    user32.IsWindowVisible.restype = ctypes.c_bool
    user32.IsWindowVisible.argtypes = [
        wintypes.HWND]
    user32.IsIconic.restype = ctypes.c_bool
    user32.IsIconic.argtypes = [
        wintypes.HWND]
    user32.GetWindowTextLengthW.restype = ctypes.c_int
    user32.GetWindowTextLengthW.argtypes = [
        wintypes.HWND]
    user32.GetWindowTextW.restype = ctypes.c_int
    user32.GetWindowTextW.argtypes = [
        wintypes.HWND,
        wintypes.LPWSTR,
        ctypes.c_int]
    user32.FindWindowW.restype = wintypes.HWND
    user32.FindWindowW.argtypes = [
        wintypes.LPCWSTR,
        wintypes.LPCWSTR]
    user32.FindWindowExW.restype = wintypes.HWND
    user32.FindWindowExW.argtypes = [
        wintypes.HWND,
        wintypes.HWND,
        wintypes.LPCWSTR,
        wintypes.LPCWSTR]
    user32.SendMessageW.restype = ctypes.c_ssize_t
    user32.SendMessageW.argtypes = [
        wintypes.HWND,
        ctypes.c_uint,
        wintypes.WPARAM,
        wintypes.LPARAM]
    user32.GetWindowThreadProcessId.restype = wintypes.DWORD
    user32.GetWindowThreadProcessId.argtypes = [
        ctypes.POINTER,
        None(wintypes.DWORD)]
    user32.ClientToScreen.restype = ctypes.c_bool
    user32.ClientToScreen.argtypes = [
        ctypes.POINTER,
        None(wintypes.POINT)]
    user32.GetClassNameW.restype = ctypes.c_int
    user32.GetClassNameW.argtypes = [
        wintypes.HWND,
        wintypes.LPWSTR,
        ctypes.c_int]
    user32.FlashWindowEx.restype = ctypes.c_bool
    
    def _FLASHWINFO():
        '''_FLASHWINFO'''
        __firstlineno__ = 70
        _fields_ = [
            ('cbSize', ctypes.c_uint),
            ('hwnd', wintypes.HWND),
            ('dwFlags', ctypes.c_uint),
            ('uCount', ctypes.c_uint),
            ('dwTimeout', ctypes.c_uint)]
        __static_attributes__ = ()

    _FLASHWINFO = None(_FLASHWINFO, '_FLASHWINFO', ctypes.Structure)
    user32.FlashWindowEx.argtypes = [
        <NODE:12>]
    kernel32.OpenProcess.restype = wintypes.HANDLE
    kernel32.OpenProcess.argtypes = [
        wintypes.DWORD,
        ctypes.c_bool,
        wintypes.DWORD]
    kernel32.VirtualAllocEx.restype = wintypes.LPVOID
    kernel32.VirtualAllocEx.argtypes = [
        wintypes.HANDLE,
        wintypes.LPVOID,
        ctypes.c_size_t,
        wintypes.DWORD,
        wintypes.DWORD]
    kernel32.VirtualFreeEx.restype = ctypes.c_bool
    kernel32.VirtualFreeEx.argtypes = [
        wintypes.HANDLE,
        wintypes.LPVOID,
        ctypes.c_size_t,
        wintypes.DWORD]
    kernel32.ReadProcessMemory.restype = ctypes.c_bool
    kernel32.ReadProcessMemory.argtypes = [
        wintypes.LPCVOID,
        wintypes.LPVOID,
        ctypes.c_size_t,
        ctypes.POINTER,
        None(ctypes.c_size_t)]
    kernel32.CloseHandle.restype = ctypes.c_bool
    kernel32.CloseHandle.argtypes = [
        wintypes.HANDLE]
    PROCESS_VM_OPERATION = 8
    PROCESS_VM_READ = 16
    PROCESS_VM_WRITE = 32
    MEM_COMMIT = 4096
    MEM_RESERVE = 8192
    MEM_RELEASE = 32768
    PAGE_READWRITE = 4
    LVM_GETITEMCOUNT = 4100
    LVM_GETITEMPOSITION = 4112
    kernel32.CreateMutexW.restype = wintypes.HANDLE
    kernel32.CreateMutexW.argtypes = [
        ctypes.c_void_p,
        ctypes.c_bool,
        wintypes.LPCWSTR]
    ERROR_ALREADY_EXISTS = 183
    user32.GetSystemMetrics.restype = ctypes.c_int
    user32.GetSystemMetrics.argtypes = [
        ctypes.c_int]
    
    def MONITORINFO():
        '''MONITORINFO'''
        __firstlineno__ = 115
        _fields_ = [
            ('cbSize', wintypes.DWORD),
            ('rcMonitor', wintypes.RECT),
            ('rcWork', wintypes.RECT),
            ('dwFlags', wintypes.DWORD)]
        __static_attributes__ = ()

    MONITORINFO = None(MONITORINFO, 'MONITORINFO', ctypes.Structure)
    MONITORINFOF_PRIMARY = 1
    MonitorEnumProc = ctypes.c_int(wintypes.HANDLE, wintypes.HANDLE, ctypes.POINTER, None(wintypes.RECT), wintypes.LPARAM)
    user32.EnumDisplayMonitors.restype = ctypes.c_bool
    user32.EnumDisplayMonitors.argtypes = [
        ctypes.POINTER,
        None(wintypes.RECT),
        MonitorEnumProc,
        wintypes.LPARAM]
    user32.GetMonitorInfoW.restype = ctypes.c_bool
    user32.GetMonitorInfoW.argtypes = [
        ctypes.POINTER,
        None(MONITORINFO)]
    SM_XVIRTUALSCREEN = 76
    SM_YVIRTUALSCREEN = 77
    SM_CXVIRTUALSCREEN = 78
SM_CYVIRTUALSCREEN = 79
_instance_mutex_handle = None

def set_dpi_aware():
    '''이 프로세스를 \'모니터별 DPI 인식(Per-Monitor DPI Aware)\'으로 선언한다.

이걸 안 하면(기본값 = DPI 인식 안 함) 배율이 100%가 아닌 화면(요즘 노트북 대부분이
125%/150% 등을 씀)에서 Windows가 좌표를 몰래 확대/축소해서 보여주는데, 이 배율이
모니터 구성마다 달라서 GetSystemMetrics/GetWindowRect로 잰 화면·작업표시줄 크기와
tkinter 창이 실제로 그려지는 위치가 서로 어긋날 수 있다. 이게 "어떤 PC에서는
포켓몬이 화면 맨 위에 붙어서 안 내려온다" 같이 PC마다 다르게 나타나는 화면 배치
버그의 흔한 원인이라, 반드시 tk.Tk() 창을 하나라도 만들기 전에 호출해야 한다.'''
    if not IS_WINDOWS:
        pass
    return None
    
    try:
        hr = ctypes.windll.shcore.SetProcessDpiAwareness(2)
        if hr == 0:
            pass
        return None
        
        try:
            ctypes.windll.user32.SetProcessDPIAware()
            return None
            continue
        except Exception:
            return None



FLASHW_ALL = 3
FLASHW_TIMERNOFG = 12
FLASHW_STOP = 0

def flash_taskbar(hwnd, count = 8, interval_ms = 500):
    '''지정한 창의 작업표시줄 아이콘을 깜빡여서 눈에 띄게 알려준다(야생 포켓몬 조우 등).
창이 이미 맨 앞에 떠 있으면(포커스 상태) Windows가 알아서 무시하고 안 깜빡인다 -
다른 작업 중일 때만 눈에 띄는 게 원래 의도이므로 정상 동작이다.
주의: overrideredirect(테두리 없는) 창은 애초에 작업표시줄에 아이콘 자체가 없는 경우가
많아서, 이 함수를 불러도 화면상 아무 변화가 없을 수 있다 - pet.py는 이 문제를 피하려고
테두리가 있는 작은 도우미 창(PetApp._taskbar_win)의 hwnd를 대신 넘겨서 사용한다.
dwTimeout을 0(=OS 기본 커서 깜빡임 속도)으로 두면, 컴퓨터의 "커서 깜빡임" 접근성 설정이
꺼져 있는 경우 아예 안 깜빡이는 것처럼 보일 수 있어서, 항상 명시적으로 간격(ms)을
지정해 그 설정과 무관하게 일정한 속도로 깜빡이게 한다.'''
    if not IS_WINDOWS:
        pass
    return False
    
    try:
        hwnd = int(hwnd)
        if not hwnd:
            pass
        return False
        
        try:
            info = _FLASHWINFO()
            info.cbSize = None(_FLASHWINFO)
            info.hwnd = hwnd
            info.dwFlags = FLASHW_ALL | FLASHW_TIMERNOFG
            info.uCount = max(1, int(count))
            info.dwTimeout = max(1, int(interval_ms))
            ctypes.byref(None(info))
            return True
        except Exception:
            return False




def stop_taskbar_flash(hwnd):
    '''flash_taskbar로 시작된 깜빡임을 즉시 멈춘다(유저가 조우 창을 열었거나, 조우를
놓쳐서 시간 초과로 사라졌을 때 호출).'''
    if not IS_WINDOWS:
        pass
    return False
    
    try:
        hwnd = int(hwnd)
        if not hwnd:
            pass
        return False
        
        try:
            info = _FLASHWINFO()
            info.cbSize = None(_FLASHWINFO)
            info.hwnd = hwnd
            info.dwFlags = FLASHW_STOP
            info.uCount = 0
            info.dwTimeout = 0
            ctypes.byref(None(info))
            return True
        except Exception:
            return False



GWL_EXSTYLE = -20
WS_EX_TOOLWINDOW = 128
WS_EX_APPWINDOW = 262144
SWP_NOMOVE = 2
SWP_NOSIZE = 1
SWP_NOZORDER = 4
SWP_NOACTIVATE = 16
SWP_FRAMECHANGED = 32

def hide_window_from_taskbar(hwnd):
    '''지정한 창이 최소화되거나(iconify) 어떤 상태가 되어도 작업표시줄에 절대 아이콘이
뜨지 않도록 "도구 창(tool window)" 스타일을 붙인다. pet.py의 숨은 도우미 창
(PetApp._taskbar_win, 예전엔 야생조우 알림용으로 잠깐 보여주다 지금은 완전히 껐음)이
일부 PC에서 withdraw/iconify 타이밍 문제로 작업표시줄에 남아있는다는 제보가 있어서,
이 스타일을 명시적으로 붙여 어떤 상황에서도 절대 안 뜨게 확실히 막는다.
64비트 파이썬에서는 GetWindowLongPtrW/SetWindowLongPtrW를(포인터 크기라 안전),
없는 구버전 환경에서는 GetWindowLongW/SetWindowLongW를 대신 쓴다.'''
    if not IS_WINDOWS:
        pass
    return False
    
    try:
        hwnd = int(hwnd)
        if not hwnd:
            pass
        return False
        
        try:
            if not getattr(user32, 'GetWindowLongPtrW', None):
                
                try:
                    getattr(user32, 'GetWindowLongPtrW', None)
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






def get_virtual_screen_rect():
    '''모든 모니터를 합친 가상 화면의 (left, top, width, height)를 돌려준다.
모니터가 하나뿐이거나 뭔가 실패하면 None을 돌려주고, 호출하는 쪽에서
기존처럼 tkinter의 winfo_screenwidth/height(주 모니터 크기)로 대체해서 쓰면 된다.'''
    if not IS_WINDOWS:
        pass
    return None
    
    try:
        left = user32.GetSystemMetrics(SM_XVIRTUALSCREEN)
        top = user32.GetSystemMetrics(SM_YVIRTUALSCREEN)
        width = user32.GetSystemMetrics(SM_CXVIRTUALSCREEN)
        height = user32.GetSystemMetrics(SM_CYVIRTUALSCREEN)
        if width <= 0 or height <= 0:
            pass
        return None
        
        try:
            return (left, top, width, height)
        except Exception:
            return None




def get_secondary_monitor_rect():
    '''주 모니터가 아닌 다른 모니터(보조 모니터) 중 첫 번째를 찾아 (left, top, width, height)로
돌려준다. 모니터가 하나뿐이거나(듀얼모니터가 아님) API 호출이 실패하면 None을 돌려주고,
호출하는 쪽에서 주 모니터 크기로 대신 쓰면 된다.'''
    if not IS_WINDOWS:
        pass
    return None
    
    try:
        found = {
            'rect': None }
        
        def _cb(hmonitor, hdc, lprect, lparam):
            '''rect'''
            pass
        # WARNING: Decompyle incomplete

        proc = MonitorEnumProc(_cb)
        user32.EnumDisplayMonitors(None, None, proc, 0)
        rect = found['rect']
        if rect and rect[2] > 0 and rect[3] > 0:
            pass
        return rect
        return None
    except Exception:
        return None



def acquire_single_instance_lock(name = 'PikaPetSingleInstanceMutex_do_bro2'):
    '''PikaPet이 이미 실행 중이면 False, 내가 첫 실행이면 True를 돌려준다.

같은 pet_state.json 저장 파일을 여러 PikaPet.exe가 동시에 열어놓고 각자
15초마다 자동저장을 하면, 나중에 저장한 쪽이 먼저 저장한 쪽의 내용을
덮어써버려서 "분명 진행했는데 다시 켜니 사라졌어요" 문제가 생길 수 있다.
이를 막기 위해 윈도우 뮤텍스로 "PikaPet은 한 번에 하나만" 규칙을 강제한다.
실패하더라도(뮤텍스 API 문제 등) 안전한 쪽(=실행 허용)으로 넘어간다.
'''
    global _instance_mutex_handle
    if not IS_WINDOWS:
        pass
    return True
    
    try:
        handle = kernel32.CreateMutexW(None, False, name)
        if not handle:
            pass
        return True
        
        try:
            _instance_mutex_handle = handle
            if None() == ERROR_ALREADY_EXISTS:
                pass
            return False
            return True
        except Exception:
            return True




def get_taskbar_rect():
    '''작업표시줄 사각형(left, top, right, bottom) 반환. 실패시 None.'''
    if not IS_WINDOWS:
        pass
    return None
    
    try:
        hwnd = user32.FindWindowW('Shell_TrayWnd', None)
        if not hwnd:
            pass
        return None
        
        try:
            rect = wintypes.RECT()
            if hwnd(ctypes.byref, None(rect)):
                
                try:
                    return (rect.left, rect.top, rect.right, rect.bottom)
                    return None
                except Exception:
                    return None





def get_window_ledges(exclude_titles = None, max_windows = 40):
    '''
현재 떠 있는 다른 프로그램 창들의 \'윗면\'을 발판 목록으로 반환.
각 원소: {"left":x, "top":y, "right":x, "title":str}
'''
    if not IS_WINDOWS:
        pass
    return []
    if not exclude_titles:
        exclude_titles
    exclude_titles = []
    ledges = []
    
    try:
        _cb = (lambda hwnd, lparam: try:
if len(ledges) >= max_windows:
passTruetry:
if not user32.IsWindowVisible(hwnd):
passTruetry:
if user32.IsIconic(hwnd):
passTruetry:
length = user32.GetWindowTextLengthW(hwnd)if length <= 0:
passTruetry:
buf = None(length + 1)user32.GetWindowTextW(hwnd, buf, length + 1)title = buf.valueif not title:
passTruetry:
if any is <common_constant>:
try:
anyfor None in exclude_titles():
if not None:
continuetry:
exclude_titles()if False:
passTruetry:
rect = wintypes.RECT()if not hwnd(ctypes.byref, None(rect)):
passTruetry:
width = rect.right - rect.leftheight = rect.bottom - rect.topif width < 80 or height < 40:
passTruetry:
ledges.append({
'title': title,
'right': rect.right,
'top': rect.top,
'left': rect.left })Trueexcept Exception:
True)()
        user32.EnumWindows(_cb, 0)
        return ledges
    except Exception:
        return 



def _find_defview():
    '''바탕화면 아이콘이 들어있는 SysListView32 핸들을 찾는다.'''
    
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






def get_desktop_icon_positions(max_icons = 60):
    '''바탕화면 아이콘들의 화면 좌표 [(x,y), ...] 를 반환. 실패시 빈 리스트.'''
    if not IS_WINDOWS:
        pass
    return []
    
    try:
        listview = _find_defview()
        if not listview:
            pass
        return []
        
        try:
            count = user32.SendMessageW(listview, LVM_GETITEMCOUNT, 0, 0)
            if count <= 0:
                pass
            return []
            
            try:
                count = min(count, max_icons)
                pid = wintypes.DWORD()
                listview(ctypes.byref, None(pid))
                h_process = kernel32.OpenProcess(PROCESS_VM_OPERATION | PROCESS_VM_READ | PROCESS_VM_WRITE, False, pid.value)
                if not h_process:
                    pass
                return []
                
                try:
                    remote_buf = kernel32.VirtualAllocEx(h_process, None, 8, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE)
                    if not remote_buf:
                        
                        try:
                            
                            try:
                                kernel32.CloseHandle(h_process)
                                return []
                                
                                try:
                                    positions = []
                                    local_buf = None(8)
                                    bytes_read = None(0)
                                    
                                    try:
                                        for i in range(count):
                                            user32.SendMessageW(listview, LVM_GETITEMPOSITION, i, remote_buf)
                                            ok = h_process(remote_buf, local_buf, 8, ctypes.byref, None(bytes_read))
                                            if not ok:
                                                continue
                                            x = ()
                                            y = None('ll', local_buf.raw)
                                            listview(ctypes.byref, None(pt))
                                            positions.append((pt.x, pt.y))
                                        
                                        try:
                                            kernel32.VirtualFreeEx(h_process, remote_buf, 0, MEM_RELEASE)
                                            
                                            try:
                                                kernel32.CloseHandle(h_process)
                                                return positions
                                                kernel32.VirtualFreeEx(h_process, remote_buf, 0, MEM_RELEASE)
                                                
                                                try:
                                                    pass
                                                except:
                                                    kernel32.CloseHandle(h_process)
                                                    
                                                    try:
                                                        pass
                                                    except Exception:
                                                        struct.unpack
                                                        return 













