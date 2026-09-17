# module.PetApp.open_pvp_lobby._poll
# source line 17830
# Recovered from bytecode; default argument values are not shown.

def _poll():
    client = state_box.get('client')
    if client is not None or state_box.get('matched'):
        return None

    try:
        msg = client.events.get_nowait()
        mtype = msg.get('type')
        if mtype == 'connected':
            continue
        if mtype == 'waiting':
            status_var.set(status_var.get() + '\n(서버 연결 완료, 상대를 기다리는 중...)')
            continue
        if mtype == 'matched':
            state_box['matched'] = True
            role = msg.get('role', 'guest')
            room = code_var.get().strip().upper()
            _cleanup_ref = state_box['client']
            state_box['client'] = None
            self._pvp_lobby_win = None
            win.destroy()
            self.open_pvp_battle(_cleanup_ref, role, room)
            return None
        if None == 'error':
            None('PikaPet', f'''참가할 수 없어요: {msg.get('message', '')}''')
            None()
            None()
            status_var.set('')
            return None
        if not None in ('conn_error', 'disconnected'):
            continue
        
            try:
                if not state_box.get('matched'):
                
                    try:
                        None('PikaPet', msg.get('message', '서버 연결이 끊어졌어요.'))
                        None()
                        None()
                        status_var.set('')
                        return None
                    except queue.Empty:
                        pass

                
                    try:
                        win.after(150, _poll)
                        return None
                    except Exception:
                        return None
