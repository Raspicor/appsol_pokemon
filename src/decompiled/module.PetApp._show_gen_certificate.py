# module.PetApp._show_gen_certificate
# source line 11168
# Recovered from bytecode; default argument values are not shown.

def _show_gen_certificate(self, gen):
    info = GEN_COMPLETE_INFO.get(gen, { })
    label = info.get('label', f'''{gen}세대''')
    rng = info.get('range', '')
    win = None(self.root)
    win.title(f'''{label} 도감 완성!''')

    try:
        win.attributes('-topmost', True)
        resolve_species_win(win, 460, 580)
        win.configure(bg = '#1c1c26')
        None(win, text = '🏆 도감 완성 인증서 🏆', font = ('맑은 고딕', 16, 'bold'), bg = '#1c1c26', fg = '#ffd54a').pack(padx = 16, pady = (24, 6))
        badge_img = draw_completion_badge(190, gen)
        badge_photo = None(badge_img)
        badge_lbl = None(win, image = badge_photo, bg = '#1c1c26')
        badge_lbl.image = badge_photo
        badge_lbl.pack(pady = (6, 14))
        None(win, text = f'''{label} ({rng}) 포켓몬을\n전부 도감에 등록했습니다!''', font = ('맑은 고딕', 13, 'bold'), bg = '#1c1c26', fg = 'white', justify = 'center').pack(padx = 20, pady = (0, 8))
        caught_n = len(self.state.get('caught', { }))
        None(win, text = f'''지금까지 누적 도감 등록: {caught_n}종''', font = ('맑은 고딕', 9), bg = '#1c1c26', fg = '#aaaaaa').pack(pady = (0, 4))
        if gen == 1:
            sub = '2세대 포켓몬들이 야생에 등장하기 시작합니다!'
        elif gen == 2:
            sub = '3세대(호연) 포켓몬들이 야생에 등장하기 시작합니다!'
        else:
            sub = '정말 대단해요! 앞으로도 새로운 도전이 기다리고 있어요.'
        None(win, text = sub, font = ('맑은 고딕', 9), bg = '#1c1c26', fg = '#8fd6ff', wraplength = 380, justify = 'center').pack(padx = 20, pady = (0, 18))
        None(win, text = '확인', width = 16, command = win.destroy).pack(pady = (0, 20))
        self._add_opacity_control(win)
        win.update_idletasks()
    
        try:
            win.grab_set()
            win.wait_window()
            return None
            except Exception:
                tk.Label
                continue
        except Exception:
            tk.Label
            continue
