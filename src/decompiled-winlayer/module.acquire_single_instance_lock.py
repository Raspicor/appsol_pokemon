# module.acquire_single_instance_lock
# source line 326
# Recovered from bytecode; default argument values are not shown.

def acquire_single_instance_lock(name):
    if not IS_WINDOWS:
        return True

    try:
        handle = kernel32.CreateMutexW(None, False, name)
        if not handle:
            return True
        _instance_mutex_handle = None
        if None() == ERROR_ALREADY_EXISTS:
            return False
        return ctypes.GetLastError
    except Exception:
        return True
