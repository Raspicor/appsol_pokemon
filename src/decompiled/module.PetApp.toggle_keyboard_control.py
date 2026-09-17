# module.PetApp.toggle_keyboard_control
# source line 9189
# Recovered from bytecode; default argument values are not shown.

def toggle_keyboard_control(self):
    self.state['keyboard_control'] = not self.state.get('keyboard_control', False)
    self._key_left = False
    self._key_right = False
    if self.state['keyboard_control']:
        self.behavior_state = 'idle'
        self.play_action('Idle', loop = True)
        self._grab_keyboard_focus()
    
        try:
            if self.tray_icon:
            
                try:
                    self.tray_icon.notify('방향키 조작 켜짐! ←/→ 로 이동, 스페이스바로 점프해보세요.\n키가 안 먹으면 포켓몬을 한 번 클릭해서 포커스를 준 뒤 다시 눌러보세요.', 'PikaPet')
                self.behavior_state = 'idle'
                self.save_state()
                return None
                except Exception:
                    continue
