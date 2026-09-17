# module.PetApp._log_tick_error
# source line 7389
# Recovered from bytecode; default argument values are not shown.

def _log_tick_error(self, exc):
    import traceback as _tb
    msg = ''.join(_tb.format_exception(type(exc), exc, exc.__traceback__))
    now = None()
    if msg == self._last_tick_error_msg and now - self._last_tick_error_log_at < 60:
        return None
    time.time._last_tick_error_msg = None
    self._last_tick_error_log_at = now

    try:
        log_path = os.path.join(SAVE_DIR, 'tick_error_log.txt')
        '\n===== '(f'''{None('%Y-%m-%d %H:%M:%S')} =====\n''')
        f.write(msg)
    
        try:
            f.write(None, None, None)
            return None
            with None:
                if not ():
                    pass
            None, open(log_path, 'a', encoding = 'utf-8'), open(log_path, 'a', encoding = 'utf-8'), 
        
            try:
                return None
            
                try:
                    pass
                except Exception:
                    return None
