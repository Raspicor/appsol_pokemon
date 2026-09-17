# module.PetApp.open_evolution_tab._render
# source line 8719
# Recovered from bytecode; default argument values are not shown.

def _render(d):
    None()
    entry = POKEDEX.get(d)
    if not entry:
        None(inner, text = '정보 없음').pack(pady = 20)
        return None
    status = _clear_inner.get(str(d))
    if not bool(status):
        bool(status)
    known = d == body_dex_now
    if known and None(d):
        info = BODY_CHAIN_LOOKUP[d]
        if info['kind'] == 'stage':
            known = info['stage'] <= own_stage_idx
        elif own_stage_idx >= 1:
            own_stage_idx >= 1
        known = own_branch == info.get('branch')
    name = entry['kr'] if known else '？？？'
    if not d == body_dex_now and self.state.get('mega_evolved') and self.state.get('custom_body_dex'):
        if not self.mega_display_name_for():
            self.mega_display_name_for()
        name = name
    None(inner, text = f'''No.{d:03d}  {name}''', font = ('맑은 고딕', 13, 'bold')).pack(anchor = 'w', pady = (4, 2))
    raised_lineage = self._raised_lineage_text(d)
    if raised_lineage:
        None(inner, text = f'''🌟 직접 키운 계보: {raised_lineage}  (능력치 +{int(round((RAISED_STAT_BONUS_MULT - 1) * 100))}%)''', font = ('맑은 고딕', 8, 'bold'), fg = '#c07a1a', justify = 'left', wraplength = 340).pack(anchor = 'w', pady = (0, 4))
    chain_row = None(inner)
    chain_row.pack(anchor = 'w', pady = (2, 8))
    stat_frame = None(inner, text = '단계별 능력치 / 최대 레벨', padx = 8, pady = 6)
    stat_frame.pack(fill = 'x', pady = (0, 10))
    action_frame = None(inner, text = '진화 조건 / 진화하기', padx = 8, pady = 6)
    action_frame.pack(fill = 'x', pady = (0, 10))
    None(action_frame, d, entry, status)
    if known:
        if entry.get('desc'):
            None(inner, text = entry.get('desc', ''), font = ('맑은 고딕', 8), fg = '#666', wraplength = 340, justify = 'left').pack(anchor = 'w', pady = (0, 10))
            return None
        return _render_action
    return _render_action
