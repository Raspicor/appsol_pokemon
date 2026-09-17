# module.PetApp.enter_ball
# source line 11410
# Recovered from bytecode; default argument values are not shown.

def enter_ball(self):
    self.state['in_ball'] = True
    self.save_state()

    try:
        self.root.withdraw()
        self._apply_companion_ball_visibility()
    
        try:
            if self.tray_icon:
            
                try:
                    self.tray_icon.update_menu()
                
                    try:
                        if self.tray_icon:
                        
                            try:
                                self.tray_icon.notify('몬스터볼 안에서 계속 자라고 있어요.\n트레이 아이콘에서 다시 꺼낼 수 있어요.', 'PikaPet')
                                return None
                                return None
                                except Exception:
                                    continue
                                except Exception:
                                    continue
                            except Exception:
                                return None
