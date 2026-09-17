# module.PvpClient.__init__
# source line 3351
# Recovered from bytecode; default argument values are not shown.

def __init__(self, addr, room):
    if not addr:
        addr
    self.addr = ''.strip()
    self.room = room
    self.events = None()
    self._send_queue = None()
    self._loop = None
    self._ws = None
    self._closing = False
    self._thread = None(target = self._thread_main, daemon = True)
    self._thread.start()
