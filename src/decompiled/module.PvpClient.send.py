# module.PvpClient.send
# source line 3362
# Recovered from bytecode; default argument values are not shown.

def send(self, msg):
    self._send_queue.put(msg)
