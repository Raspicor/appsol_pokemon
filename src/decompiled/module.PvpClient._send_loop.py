# module.PvpClient._send_loop
# source line 3420
# Recovered from bytecode; default argument values are not shown.

async def _send_loop(self, ws):
    try:
        msg = self._send_queue.get_nowait()
        if msg is None:
            return None
    
        try:
            yield None
        
            try:
                continue
                <NODE:28>
                continue
                except queue.Empty:
                    yield None
                    continue
                    <NODE:28>
                    continue
            
                try:
                    continue
                except Exception:
                    return None
