# module.PvpClient._main
# source line 3381
# Recovered from bytecode; default argument values are not shown.

async def _main(self):
    try:
        import websockets
        uri = f'''ws://{self.addr}'''
    
        try:
            yield None
        
            try:
                continue
                None() = asyncio.get_running_loop
                self.events.put({
                    'type': 'connected' })
                yield None
                continue
                <NODE:28>
                send_task = None(self._send_loop(ws))
                yield None
                continue
                raw = asyncio.ensure_future
                msg = None(raw)
                self.events.put(msg)
                continue
                except Exception:
                    ws.send
                    self.events.put({
                        'message': 'websockets 패키지가 설치되어 있지 않아요.\n명령프롬프트(cmd)에서 pip install websockets 를 먼저 실행해주세요.',
                        'type': 'conn_error' })
                    return None
            
                try:
                    continue
                    continue
                    continue
                    except Exception:
                        ws.send
                        continue
                    send_task.cancel()
                    yield None
                    continue
                    <NODE:28>
                except (Exception, asyncio.CancelledError):
                    ws.send
                except (Exception, asyncio.CancelledError):
                
                    try:
                        yield None
                    
                        try:
                            continue
                            <NODE:28>
                        except:
                            with None:
                                yield None
                                continue
                                if not <NODE:28>:
                                    pass
                            None, websockets.connect(uri, open_timeout = 8, close_timeout = 3), websockets.connect(uri, open_timeout = 8, close_timeout = 3), 
                        
                            try:
                                ws
                                <NODE:28>
                                None, websockets.connect(uri, open_timeout = 8, close_timeout = 3), websockets.connect(uri, open_timeout = 8, close_timeout = 3), 
                            except:
                            
                                try:
                                    pass
                                except Exception:
                                    e = ws
                                    self.events.put({
                                        'message': f'''서버({self.addr})에 연결하지 못했어요: {e}\n주소가 맞는지, pvp_server.py가 실행 중인지 확인해주세요.''',
                                        'type': 'conn_error' })
                                    e = None
                                    del e
                                    return None
                                    e = None
                                    del e
                                    self.events.put({
                                        'type': 'disconnected' })
                                    return None
