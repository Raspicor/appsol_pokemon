# module.PetApp.open_infinite_stone._on_hit
# source line 5849
# Recovered from bytecode; default argument values are not shown.

def _on_hit(_evt):
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
