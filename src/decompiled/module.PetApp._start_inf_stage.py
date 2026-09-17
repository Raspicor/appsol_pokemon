# module.PetApp._start_inf_stage
# source line 14420
# Recovered from bytecode; default argument values are not shown.

def _start_inf_stage(self, mode, reward_msg, reuse_win):
    stage = int(self.state.get('inf_meter_stage', { }).get(mode, 1))
    if stage > INF_STAGE_CAP:
    
        try:
            if reuse_win is not None and reuse_win.winfo_exists():
            
                try:
                    reuse_win.destroy()
                    None('PikaPet', f'''♾ 지금은 {INF_STAGE_CAP}스테이지까지만 열려있어요.\n이후 스테이지는 업데이트 예정이니 조금만 기다려주세요!''')
                    return None
                    player_roster = self._inf_build_player_roster(mode)
                    enemy_roster = self._inf_build_enemy_roster(mode, stage)
                    cycle = ()
                    gen = inf_stage_cycle_info(stage)
                    pos_in_block = messagebox.showinfo
                    _pos_in_cycle = None
                    if kind == 'boss':
                        pass
                    elif kind == 'mirror':
                        title += f''' ({gen}세대 전설 군단전!)'''
                    win = None
                    if reuse_win is not None:
                    
                        try:
                            if reuse_win.winfo_exists():
                            
                                try:
                                    win = reuse_win
                                    if win is None:
                                        win = None(self.root)
                                    
                                        try:
                                            win.attributes('-topmost', True)
                                        
                                            try:
                                                pos = getattr(self, '_inf_win_pos', None)
                                                if pos:
                                                    win.geometry(f'''+{pos[0]}+{pos[1]}''')
                                                else:
                                                
                                                    try:
                                                        left = getattr(self, 'screen_left', 0)
                                                        top = getattr(self, 'screen_top', 0)
                                                        sw = getattr(self, 'screen_w', self.root.winfo_screenwidth())
                                                        sh = getattr(self, 'screen_h', self.root.winfo_screenheight())
                                                        win.geometry(f'''+{int(left + sw * 0.5 - 230)}+{int(top + sh * 0.5 - 280)}''')
                                                        if mode == 'attack':
                                                            mode == 'attack'
                                                        attack_ult_allowed = kind == 'mirror'
                                                        for None in :
                                                            pass
                                                        for None in :
                                                            pass
                                                        for None in :
                                                            pass
                                                        for None in :
                                                            pass
                                                        if mode == 'attack':
                                                            mode == 'attack'
                                                        enemy_roster, m[, [], ]['p_active']['e_active']['p_ult_used']['ult_use_count']['flags'] = enemy_roster, m[, [], ]['p_active']['e_active']['p_ult_used']['ult_use_count']
                                                        win.protocol('WM_DELETE_WINDOW', (lambda : self._gym_concede(gctx)))
                                                        self._code_build_ui(gctx)
                                                        return None
                                                        except Exception:
                                                            enemy_roster, m[, [], ]['p_active']['e_active']
                                                            continue
                                                        except Exception:
                                                            enemy_roster, m[, [], ]['p_active']['e_active']
                                                            win = None
                                                            continue
                                                        except Exception:
                                                            enemy_roster, m[, [], ]['p_active']['e_active']
                                                            continue
                                                    except Exception:
                                                        f'''♾ {INF_MODE_LABEL.get(mode, mode)} - 스테이지 {stage}'''
                                                        continue
