# module.PvpClient._thread_main
# source line 3375
# Recovered from bytecode; default argument values are not shown.

def _thread_main(self):
    try:
        None(self._main())
        return None
    except Exception:
        e = None
        self.events.put({
            'message': f'''연결 스레드 오류: {e}''',
            'type': 'conn_error' })
        e = None
        del e
        return None
        e = None
        del e
