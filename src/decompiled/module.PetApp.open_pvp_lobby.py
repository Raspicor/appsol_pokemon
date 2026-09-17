# module.PetApp.open_pvp_lobby
# source line 17683
# Recovered from bytecode; default argument values are not shown.

def open_pvp_lobby(self):
    if getattr(self, '_pvp_lobby_win', None) is not None:
    
        try:
            self._pvp_lobby_win.lift()
            return None
            win = None(self.root)
            self._pvp_lobby_win = win
            win.title('🌐 온라인 대결 (베타)')
        
            try:
                win.attributes('-topmost', True)
                resolve_species_win(win, 440, 470)
                body = None(win, padx = 14, pady = 12)
                body.pack(fill = 'both', expand = True)
                None(body, text = '🌐 온라인 대결 (베타)', font = ('맑은 고딕', 13, 'bold')).pack(pady = (0, 4))
                None(body, text = '실시간으로 다른 PikaPet 유저와 1:1로 싸워요. 나와 상대가 각자 자기\n컴퓨터에서 PikaPet을 켜고, 중계서버 하나(꼭 둘 중 한쪽 컴퓨터일\n필요는 없음)를 거쳐 서로 연결돼요.', font = ('맑은 고딕', 8), fg = '#666', justify = 'left', wraplength = 400).pack(pady = (0, 8))
                is_frozen = getattr(sys, 'frozen', False)
                tool_row = None(body)
                tool_row.pack(fill = 'x', pady = (0, 8))
            
                def _open_ngrok():
                    '''https://ngrok.com'''
                
                    try:
                        None('https://ngrok.com')
                        return None
                    except Exception:
                        None('PikaPet', '브라우저를 여는 데 실패했어요. https://ngrok.com 을 직접 열어주세요.')
                        return None


                if not is_frozen:
                
                    def _install_websockets():
                        '''start "PikaPet 온라인대결 설치" cmd /k "pip install websockets"'''
                    
                        try:
                            cmd = 'start "PikaPet 온라인대결 설치" cmd /k "pip install websockets"'
                            None(cmd, shell = True)
                            return None
                        except Exception:
                            e = None
                            None('PikaPet', f'''설치 창을 여는 데 실패했어요: {e}\n직접 cmd를 열고 아래를 입력해주세요:\npip install websockets''')
                            e = None
                            del e
                            return None
                            e = None
                            del e


                    None(tool_row, text = '🧩 필요한 프로그램 설치 (최초 1회)', font = ('맑은 고딕', 8), command = _install_websockets).pack(side = 'left')
                None(tool_row, text = '🔗 ngrok.com 열기', font = ('맑은 고딕', 8), command = _open_ngrok).pack(side = 'left', padx = (6, 0))
                None(tool_row, text = '📜 지난 기록', font = ('맑은 고딕', 8), command = self.open_pvp_history).pack(side = 'left', padx = (6, 0))
                if not is_frozen:
                    None(body, text = '설치 버튼을 누르면 검은 cmd 창이 뜨고 자동으로 설치가 진행돼요.\n설치가 끝났다는 문구가 뜨면 그 창은 닫아도 돼요(최초 1회만 하면 됨).', font = ('맑은 고딕', 7), fg = '#999', justify = 'left', wraplength = 400).pack(anchor = 'w', pady = (0, 8))
                addr_row = None(body)
                addr_row.pack(fill = 'x', pady = (0, 10))
                None(addr_row, text = '서버 주소', font = ('맑은 고딕', 9)).pack(side = 'left')
                addr_var = None(value = self.state.get('pvp_server_addr', ''))
                addr_entry = None(addr_row, textvariable = addr_var, font = ('맑은 고딕', 9))
                addr_entry.pack(side = 'left', fill = 'x', expand = True, padx = (6, 0))
                None(body, text = '예) 192.168.0.5:8765  또는  0.tcp.ngrok.io:12345', font = ('맑은 고딕', 7), fg = '#999').pack(anchor = 'w', pady = (0, 10))
                status_var = None(value = '')
                status_lbl = None(body, textvariable = status_var, font = ('맑은 고딕', 9, 'bold'), fg = '#1a4a8a', wraplength = 360, justify = 'left')
                status_lbl.pack(fill = 'x', pady = (0, 8))
                code_row = None(body)
                code_row.pack(fill = 'x', pady = (0, 6))
                None(code_row, text = '참가할 방 코드', font = ('맑은 고딕', 9)).pack(side = 'left')
                code_var = None()
                code_entry = None(code_row, textvariable = code_var, font = ('맑은 고딕', 10, 'bold'), width = 10)
                code_entry.pack(side = 'left', padx = (6, 0))
                btn_row = None(body)
                btn_row.pack(fill = 'x', pady = (8, 0))
                host_btn = None(btn_row, text = '🆕 방 만들기 (호스트)', width = 20)
                join_btn = None(btn_row, text = '🔑 코드로 참가', width = 16)
                host_btn.pack(side = 'left')
                join_btn.pack(side = 'left', padx = (6, 0))
                help_row = None(body)
                help_row.pack(fill = 'x', pady = (6, 0))
                None(help_row, text = '❓ 사용법', font = ('맑은 고딕', 8), command = self.open_pvp_help).pack(side = 'left')
                state_box = {
                    'matched': False,
                    'client': None }
            
                def _cleanup_client():
                    '''client'''
                    c = state_box.get('client')
                    if c is not None:
                    
                        try:
                            c.close()
                            state_box['client'] = None
                            return None
                        except Exception:
                            continue


            
                def _on_close():
                    None()
                    self._pvp_lobby_win = None
                    win.destroy()

                win.protocol('WM_DELETE_WINDOW', _on_close)
            
                def _start(is_host):
                    '''PikaPet'''
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

            
                def _reset_buttons():
                    '''normal'''
                
                    try:
                        host_btn.configure(state = 'normal')
                        join_btn.configure(state = 'normal')
                        return None
                    except Exception:
                        return None


            
                def _poll():
                    '''client'''
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




                host_btn.configure(command = (lambda : None(True)))
                join_btn.configure(command = (lambda : None(False)))
                return None
                except Exception:
                    tk.Frame
                    continue
            except Exception:
                continue
