# module.PetApp._gym_finish
# source line 17377
# Recovered from bytecode; default argument values are not shown.

def _gym_finish(self, gctx, won, conceded):
    flags = gctx['flags']
    if flags['ended']:
        return None
    flags['ended'] = None
    flags['locked'] = True
    win = gctx['win']
    gym_idx = gctx['gym_idx']
    g = gctx['gym']
    fun_mode = gctx.get('fun_mode', False)
    if fun_mode:
    
        try:
            win.destroy()
            if won:
                None('PikaPet', f'''🎮 재미 도전 결과: {g['name']}을(를) 이겼어요! (보상은 없어요, 그냥 재미로 한 거예요 😄)''')
                return None
            if not None:
                None('PikaPet', f'''🎮 재미 도전 결과: {g['name']}에서 졌어요! (보상이 없으니 부담 없이 또 도전해보세요)''')
            return None
            if won:
                badges = self.state.setdefault('gym_badges', [])
                newly = gym_idx not in badges
                if newly:
                    badges.append(gym_idx)
                    self.save_state()
            
                try:
                    win.destroy()
                    if newly:
                        self._show_gym_victory_popup(g)
                        return None
                    None('PikaPet', f'''{g['name']}을(를) 다시 한번 이겼어요! (뱃지는 이미 갖고 있어요)''')
                    return None
                
                    try:
                        win.destroy()
                        if not conceded:
                            None('PikaPet', f'''{g['name']}에서 졌어요... 팀을 더 키워서 다시 도전해보세요!\n(진 건 아무 불이익이 없으니 언제든 다시 도전할 수 있어요)''')
                            return None
                        return messagebox.showinfo.showinfo
                        except Exception:
                            continue
                        except Exception:
                            continue
                    except Exception:
                        continue
