# module.PetApp.open_pokedex._show
# source line 16129
# Recovered from bytecode; default argument values are not shown.

def _show(idx):
    d = ()
    status = rows[idx]
    if d is None:
        return None
    status = None
    caught = self.state.get('caught', { })
    pinned_dex = self.starter_stage_conf().get('dex')
    is_pinned = d == pinned_dex
    entry = POKEDEX[d]

    try:
        aset = None(sprite_folder_path(entry['en']))
        frame = aset.frame(entry['idle'], 0, spriteanim.DIR_DOWN)
        types_txt = (lambda .0: for t in .0:
    TYPE_KR.get(t, t).0)(entry.get('types', [
            entry.get('element', 'normal')])())
        tag = ''
        if is_pinned:
            tag = '\n🌟 원래 스타터 포켓몬 (고정, 진행도 계속 유지됨)'
        elif entry.get('chain_len', 1) >= 3 and entry.get('stage', 0) == entry.get('chain_len', 1) - 1:
            tag = '\n🌟 3단계 진화의 최종 형태'
        elif entry.get('legendary'):
            tag = '\n⭐ 전설의 포켓몬'
        if not self.state.get('custom_body_dex'):
            self.state.get('custom_body_dex')
        if int(d) == int(-1):
            tag += '\n🏠 지금 화면에 나와있는 본체예요'
        raised_lineage = self._raised_lineage_text(d)
        if raised_lineage:
            tag += f'''\n🌟 직접 키운 계보: {raised_lineage}'''
        if status == 'caught':
            lv = self.player_level() if is_pinned else caught.get(str(d), { }).get('level', 1)
            lock_tag = '\n🔒 잠금됨 (다시 잡아도 기록 유지)' if is_dex_locked(self.state, d) else ''
            disp_kr = entry['kr']
            if not is_pinned and self.state.get('mega_evolved') and self.state.get('custom_body_dex'):
                if not self.mega_display_name_for():
                    self.mega_display_name_for()
                disp_kr = disp_kr
            name_var.set(f'''No.{d:03d} {disp_kr}\n({types_txt} 타입, Lv.{lv}){tag}{lock_tag}''')
            if not is_pinned:
                is_pinned
                if not self.state.get('custom_body_dex'):
                    self.state.get('custom_body_dex')
            is_active_body1 = int(d) == int(-1)
            stat_var.set(f'''HP {bs_disp['hp']}  공격 {bs_disp['atk']}  방어 {bs_disp['def']}  크리티컬 {bs_disp['crit']:.0f}%\n{stat_note}\n필살기: {entry.get('ultimate', '?')}''')
            bd = companion_synergy_breakdown([
                d], caught)
            lock_btn.configure(text = '🔓 잠금 해제' if is_dex_locked(self.state, d) else '🔒 잠금 설정', state = tk.NORMAL)
        elif status == 'seen':
            name_var.set(f'''No.{d:03d} ？？？\n({types_txt} 타입, 아직 못 잡음){tag}''')
            stat_var.set('만난 적은 있지만 아직 못 잡았어요. 능력치는 잡은 뒤에 볼 수 있어요.')
            equip_bonus_var.set('')
            lock_btn.configure(text = '🔒 잠금 설정', state = tk.DISABLED)
        else:
            name_var.set(f'''No.{d:03d} ？？？？？？\n(아직 만나지 못함)''')
            stat_var.set('아직 만난 적 없는 포켓몬이에요.')
            equip_bonus_var.set('')
            lock_btn.configure(text = '🔒 잠금 설정', state = tk.DISABLED)
        desc_label.configure(text = entry.get('desc', '') if status else '')
        None(d, status, entry)
    
        try:
            None()
            return None
            except Exception:
                _update_legend_token_btn
                frame = None
                continue
        except Exception:
            int(d) if bd else None
            return None
