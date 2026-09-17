# module.PetApp.open_infinite_stone
# source line 5736
# Recovered from bytecode; default argument values are not shown.

def open_infinite_stone(self):
    win = None(self.root)
    win.title('⛏ 무한의 돌')
    resolve_species_win(win, 300, 420)

    try:
        win.attributes('-topmost', True)
        state_holder = {
            'broken': bool(self.state.get('infinite_stone_broken')) }
    
        def _fmt(n):
            ''','''
            return f'''{int(n):,}'''

        None(win, text = '⛏ 무한의 돌', font = ('맑은 고딕', 13, 'bold')).pack(pady = (10, 1))
        None(win, text = '돌을 계속 클릭해보세요! 클릭할 때마다 지금 최종공격력만큼\n데미지가 들어가요 (단순공격만 해당, 크리티컬 없음).', font = ('맑은 고딕', 8), fg = '#666', justify = 'center', wraplength = 280).pack(pady = (0, 4))
        dmg_var = None()
        dmg_lbl = None(win, textvariable = dmg_var, font = ('맑은 고딕', 12, 'bold'), fg = '#a03030')
        dmg_lbl.pack(pady = (0, 1))
        hit_var = None(value = '')
        hit_lbl = None(win, textvariable = hit_var, font = ('맑은 고딕', 10, 'bold'), fg = '#ff6a00')
        hit_lbl.pack()
        img_holder = None(win, width = 240, height = 210)
        img_holder.pack(pady = (4, 4))
        img_holder.pack_propagate(False)
        img_label = None(img_holder, cursor = 'hand2')
        img_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
        size_row = None(win)
        size_row.pack(pady = (0, 2))
        None(size_row, text = '돌 크기', font = ('맑은 고딕', 8)).pack(side = 'left', padx = (0, 4))
        size_var = None(value = int(self.state.get('infinite_stone_size', 130)))
        size_val_var = None(value = f'''{size_var.get()}px''')
    
        def _on_size_change(_v = None):
            '''infinite_stone_size'''
            self.state['infinite_stone_size'] = size_var.get()
            size_val_var.set(f'''{size_var.get()}px''')
            self.save_state()
            None()

        None(size_row, from_ = 60, to = 200, resolution = 10, orient = 'horizontal', length = 140, variable = size_var, showvalue = False, command = _on_size_change).pack(side = 'left')
        None(size_row, textvariable = size_val_var, font = ('맑은 고딕', 8, 'bold'), width = 5).pack(side = 'left', padx = (4, 0))
        color_row = None(win)
        color_row.pack(pady = (0, 2))
        None(color_row, text = '돌 색상', font = ('맑은 고딕', 8)).pack(side = 'left', padx = (0, 4))
        color_var = None(value = self.state.get('infinite_stone_color_mode', 'color'))
    
        def _apply_text_color():
            '''흑백 모드면 데미지 숫자 글자색도 원래 빨강/주황 대신 검정으로 맞춘다.'''
            if color_var.get() == 'gray':
                dmg_lbl.configure(fg = '#111')
                hit_lbl.configure(fg = '#111')
                return None
            None.configure(fg = '#a03030')
            hit_lbl.configure(fg = '#ff6a00')

    
        def _on_color_change():
            '''infinite_stone_color_mode'''
            self.state['infinite_stone_color_mode'] = color_var.get()
            self.save_state()
            None()
            None()

        None(color_row, text = '원본', variable = color_var, value = 'color', font = ('맑은 고딕', 8), command = _on_color_change).pack(side = 'left')
        None(color_row, text = '흑백', variable = color_var, value = 'gray', font = ('맑은 고딕', 8), command = _on_color_change).pack(side = 'left')
        status_var = None()
        None(win, textvariable = status_var, font = ('맑은 고딕', 9), fg = '#1a6b1a', wraplength = 270, justify = 'center').pack(pady = (2, 0))
    
        def _next_milestone_text():
            '''infinite_stone_damage'''
            cur = self.state.get('infinite_stone_damage', 0)
            for None in INFINITE_STONE_MILESTONES:
                threshold = ()
                tid = None
                if not cur < threshold:
                    continue
                return '다음 목표: ', f'''{label} (앞으로 {None(threshold - cur)} 더!)'''
            return '모든 단계를 달성했어요!'

    
        def _update_status():
            '''broken'''
            if state_holder['broken']:
                status_var.set('🎉 무한의 돌 시즌1 클리어! 돌이 완전히 부서졌어요.\n다음 시즌은 업데이트 예정입니다.')
                return None
            _next_milestone_text(None())

    
        def _render_image():
            '''broken'''
            img = load_infinite_stone_image(state_holder['broken'], target_h = size_var.get(), grayscale = color_var.get() == 'gray')
            tkimg = None(img)
            img_label.image = tkimg
            img_label.configure(image = tkimg)

    
        def _shake(step = 0):
            offsets = [
                -6,
                6,
                -4,
                4,
                -2,
                0]
            if step >= len(offsets):
                return None
        
            try:
                img_label.place(relx = 0.5, rely = 0.5, anchor = 'center', x = offsets[step])
                win.after(35, (lambda : None(step + 1)))
                return None
            except Exception:
                return None


    
        def _on_hit(_evt = None):
            '''broken'''
            if state_holder['broken']:
                return None
            dmg = None(round(self.current_final_atk() * (1 + title_stone_dmg_bonus_pct(self.state) / 100)))
            total = self.state.get('infinite_stone_damage', 0) + dmg
            self.state['infinite_stone_damage'] = total
            '누적 데미지: '(f'''{None(total)}''')
            '- '(f'''{None(dmg)}!''')
            None()
            msgs = self._check_new_titles()
            if total >= INFINITE_STONE_BREAK_DAMAGE:
                total >= INFINITE_STONE_BREAK_DAMAGE
            just_broke = not state_holder['broken']
            if just_broke:
                state_holder['broken'] = True
                self.state['infinite_stone_broken'] = True
                None()
            self.save_state()
            None()
            if msgs:
                None('PikaPet', '\n'.join(msgs))
            if just_broke:
                None('PikaPet', '🎉 무한의 돌이 완전히 부서졌습니다!\n시즌1 클리어예요. 다음 시즌은 업데이트 예정입니다.')
                return None
            return messagebox.showinfo

        img_label.bind('<Button-1>', _on_hit)
        '누적 데미지: '(f'''{None(self.state.get('infinite_stone_damage', 0))}''')
        None()
        None()
        None()
        None(win, text = '닫기', command = win.destroy).pack(pady = (8, 8))
        self._add_opacity_control(win)
        return None
    except Exception:
        continue
