# module.PetApp.open_pvp_help
# source line 17875
# Recovered from bytecode; default argument values are not shown.

def open_pvp_help(self):
    if getattr(self, '_pvp_help_win', None) is not None:
    
        try:
            self._pvp_help_win.lift()
            return None
            win = None(self.root)
            self._pvp_help_win = win
            win.title('❓ 온라인 대결 사용법')
        
            try:
                win.attributes('-topmost', True)
                resolve_species_win(win, 420, 480)
                body = None(win, padx = 14, pady = 12)
                body.pack(fill = 'both', expand = True)
                None(body, text = '❓ 온라인 대결 사용법', font = ('맑은 고딕', 12, 'bold')).pack(pady = (0, 8))
                text = "① 중계서버(딱 한 곳)\n누군가 한 명이 컴퓨터에서 pvp_server.py를 켜둬야 해요. 계속 켜져 있어야 하니 보통 관리자 한 명(또는 항상 켜진 서버)이 맡아요.\n\n② 서버 주소 알아내기\n같은 와이파이면 ipconfig로 나온 IP:8765, 인터넷 너머면 ngrok으로 만든 주소를 씁니다.\n\n③ 유저는 그냥 PikaPet만 켜면 돼요\nexe로 받은 사람은 python이나 pip 아무것도 설치할 필요 없어요. 펫 우클릭 → 🌐 온라인 대결 → 서버 주소만 입력하면 끝.\n\n④ 방 만들기 / 참가하기\n먼저 온 사람이 '🆕 방 만들기'를 누르면 방 코드가 나와요. 그 코드를 상대에게 알려주면, 상대는 '🔑 코드로 참가'에 그 코드를 입력해요.\n\n⑤ 매칭되면 자동으로 대결 화면으로 넘어가요\n서로 스탯을 주고받은 뒤, 호스트가 먼저 공격하고 번갈아 턴이 진행돼요.\n\n⑥ 안 될 때\n- '접속 실패'가 뜨면: 서버 주소가 정확한지, pvp_server.py가 여전히 켜져 있는지 확인해주세요.\n- 방화벽이 막을 수 있어요: 서버 켠 컴퓨터의 방화벽에서 8765 포트를 허용해주세요."
                None(body, text = text, font = ('맑은 고딕', 9), justify = 'left', wraplength = 380, anchor = 'w').pack(fill = 'both', expand = True)
            
                def _on_close():
                    self._pvp_help_win = None
                    win.destroy()

                win.protocol('WM_DELETE_WINDOW', _on_close)
                None(body, text = '닫기', command = _on_close).pack(pady = (10, 0))
                self._add_opacity_control(win)
                return None
                except Exception:
                    tk.Label
                    continue
            except Exception:
                continue
