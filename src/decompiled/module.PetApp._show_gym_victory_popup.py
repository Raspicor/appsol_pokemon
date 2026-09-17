# module.PetApp._show_gym_victory_popup
# source line 17423
# Recovered from bytecode; default argument values are not shown.

def _show_gym_victory_popup(self, g):
    win = None(self.root)
    win.title(f'''{g['name']} 클리어!''')

    try:
        win.attributes('-topmost', True)
        resolve_species_win(win, 400, 420)
        win.configure(bg = '#1c1c26')
        None(win, text = f'''🏅 {g['badge_kr']} 획득! 🏅''', font = ('맑은 고딕', 15, 'bold'), bg = '#1c1c26', fg = '#ffd54a').pack(padx = 16, pady = (26, 8))
        badge_img = load_static_image(gym_badge_image_path(g), target_h = 120)
        if badge_img is None:
            region_tier = {
                'hoenn': 3,
                'johto': 2,
                'kanto': 1 }.get(g['region'], 1)
            badge_img = draw_completion_badge(150, region_tier)
        badge_photo = None(badge_img)
        badge_lbl = None(win, image = badge_photo, bg = '#1c1c26')
        badge_lbl.image = badge_photo
        badge_lbl.pack(pady = (6, 14))
        None(win, text = f'''{g['name']}을(를) 이겼습니다!''', font = ('맑은 고딕', 12, 'bold'), bg = '#1c1c26', fg = 'white').pack(pady = (0, 6))
        held = len(gym_badges_held(self.state))
        None(win, text = f'''보유 뱃지 {held}/{len(GYM_LEADERS)}   최종공격력 +{gym_badge_atk_bonus_pct(self.state):.1f}%''', font = ('맑은 고딕', 9), bg = '#1c1c26', fg = '#8fd6ff').pack(pady = (0, 18))
        None(win, text = '확인', width = 16, command = win.destroy).pack(pady = (0, 20))
        self._add_opacity_control(win)
        win.update_idletasks()
    
        try:
            win.grab_set()
            return None
            except Exception:
                tk.Label
                continue
        except Exception:
            tk.Label
            return None
