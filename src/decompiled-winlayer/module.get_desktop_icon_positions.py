# module.get_desktop_icon_positions
# source line 454
# Recovered from bytecode; default argument values are not shown.

def get_desktop_icon_positions(max_icons):
    if not IS_WINDOWS:
        return []

    try:
        listview = _find_defview()
        if not listview:
            return []
        count = None.SendMessageW(listview, LVM_GETITEMCOUNT, 0, 0)
        if count <= 0:
            return []
        count = None(count, max_icons)
        pid = wintypes.DWORD()
        listview(ctypes.byref, None(pid))
        h_process = kernel32.OpenProcess(PROCESS_VM_OPERATION | PROCESS_VM_READ | PROCESS_VM_WRITE, False, pid.value)
        if not h_process:
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
