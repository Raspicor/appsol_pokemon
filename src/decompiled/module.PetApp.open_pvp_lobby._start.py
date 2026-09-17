# module.PetApp.open_pvp_lobby._start
# source line 17796
# Recovered from bytecode; default argument values are not shown.

def _start(is_host):
    addr = addr_var.get().strip()
    if not addr:
        None('PikaPet', '서버 주소를 먼저 입력해주세요.')
        return None
    self.state['pvp_server_addr'] = None
    self.save_state()
    if is_host:
        room = pvp_random_room_code()
        code_var.set(room)
    else:
        room = code_var.get().strip().upper()
        if not room:
            None('PikaPet', '참가할 방 코드를 입력해주세요.')
            return None
        None()
        client = PvpClient(addr, room)
        state_box['client'] = client
        state_box['matched'] = False
        host_btn.configure(state = 'disabled')
        join_btn.configure(state = 'disabled')
        if is_host:
            status_var.set(f'''방을 만들었어요! 방 코드: {room}\n이 코드를 상대에게 알려주고, 상대가 참가할 때까지 기다려요...''')
        else:
            status_var.set(f'''\'{room}\' 방에 접속하는 중...''')
    None()
