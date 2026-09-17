# module.PvpClient.close
# source line 3365
# Recovered from bytecode; default argument values are not shown.

def close(self):
    self._closing = True
    self._send_queue.put(None)
    ws = self._ws
    loop = self._loop
    if loop is not None:
        if ws is not None:
        
            try:
                None(ws.close(), loop)
                return None
                return None
                return None
            except Exception:
                return None
