# module.PetApp.open_evolution_tab._render_action
# source line 8513
# Recovered from bytecode; default argument values are not shown.

def _render_action(parent, d, entry, status):
    is_body_dex = d == body_dex_now
    if is_body_dex:
        sp = SPECIES[own_species]
        max_stage = 1 if sp.get('branching') else len(sp['stages']) - 1
        if own_stage_idx >= max_stage:
            None(parent, text = '🏠 본체 · 이미 최종 진화 단계예요.', font = ('맑은 고딕', 8), fg = '#888').pack(anchor = 'w')
            return None
        None(parent, text = f'''🏠 지금 본체(내 포켓몬)예요.\n{self.evolution_progress_text()}''', font = ('맑은 고딕', 8, 'bold'), fg = '#1a6b1a', justify = 'left', wraplength = 340).pack(anchor = 'w')
        ready = self.evolution_ready()
        if sp.get('branching'):
        
            def _do_evolve(branch, branch_kr):
                '''PikaPet'''
                if not self.evolution_ready():
                    None('PikaPet', '아직 진화 조건을 채우지 못했어요.')
                    return None
                if not None('PikaPet', f'''정말 {branch_kr}(으)로 진화시킬까요?\n(진화 후에는 되돌릴 수 없어요)'''):
                    return None
                None.askyesno.evolve(forced_branch = branch)
                None()

            if eevee_friendship_ready(self.state):
                hour = None().tm_hour
                None(parent, text = f'''💞 친밀도 조건 달성! (애정도 {self.state.get('affection', 50):.0f} / {EEVEE_FRIENDSHIP_AFFECTION_MIN}, 불물전기 훈련 안 치우침) 에스피언·블래키 중 골라 진화할 수 있어요.''', font = ('맑은 고딕', 8), fg = '#a83a8a', justify = 'left', wraplength = 340).pack(anchor = 'w', pady = (4, 2))
                None(parent) = tk.Frame
                row.pack(anchor = 'w', pady = (0, 4))
                None(row, text = '☀ 에스피언으로 진화!', state = tk.NORMAL if is_day else tk.DISABLED, command = (lambda : None('psychic', '에스피언'))).pack(side = 'left', padx = (0, 4))
                None(row, text = '🌙 블래키로 진화!', state = tk.DISABLED if is_day else tk.NORMAL, command = (lambda : None('dark', '블래키'))).pack(side = 'left')
                None(parent, text = '(낮이라 에스피언만 가능해요. 밤에 다시 와보세요.)' if is_day else '(밤이라 블래키만 가능해요. 낮에 다시 와보세요.)', font = ('맑은 고딕', 7), fg = '#888').pack(anchor = 'w')
                return None
            et = None.Label.state.get('element_train', {
                'electric': 0,
                'water': 0,
                'fire': 0 })
            self._predict_eevee_branch() = tk.Label if tied else tk.Label
            predicted_kr = sp['branches'][predicted]['kr']
            None(parent, text = f'''지금 진화하면 예상: {predicted_kr} (원소 훈련 기준)''', font = ('맑은 고딕', 8), fg = '#555').pack(anchor = 'w', pady = (4, 2))
            None(parent, text = '진화!', state = tk.NORMAL if ready else tk.DISABLED, command = (lambda p = predicted, pk = predicted_kr: None(p, pk))).pack(anchor = 'w', pady = (2, 4))
            return None
    
        def _do_evolve_body():
            '''PikaPet'''
            if not self.evolution_ready():
                None('PikaPet', '아직 진화 조건을 채우지 못했어요.')
                return None
            if not None('PikaPet', '정말 진화시킬까요? (되돌릴 수 없어요)'):
                return None
            None.askyesno.evolve()
            None()

        None(parent, text = '진화!', state = tk.NORMAL if ready else tk.DISABLED, command = _do_evolve_body).pack(anchor = 'w', pady = (4, 4))
        return None
    custom_dex_now = None.state.get('custom_body_dex')
    if custom_dex_now is not None and int(custom_dex_now) == d:
        cstatus = self.companion_evolution_status(d)
        None(parent, text = f'''레벨: Lv.{self.body1_effective_level()} (이 종 자신의 레벨/능력치를 그대로 써요,\n원래 스타터 레벨과는 무관해요)''', font = ('맑은 고딕', 8), fg = '#3a5a9a', justify = 'left', wraplength = 340).pack(anchor = 'w', pady = (0, 4))
        if not cstatus.get('evolvable'):
            None(parent, text = f'''🔁 지금 화면에 나와있는 본체예요. {cstatus.get('reason', '')}''', font = ('맑은 고딕', 8), fg = '#888', wraplength = 340, justify = 'left').pack(anchor = 'w')
            return None
        nxt = tk.Label['next_entry']
        None(parent, text = f'''🔁 지금 화면에 나와있는 본체예요 (원래 스타터의 레벨/진행도는 별개로 계속 유지돼요).\n다음 진화: {nxt.get('kr', '?')}\n진행도: {min(cstatus['elapsed_days'], cstatus['days_needed']):.1f} / {cstatus['days_needed']:.1f}일  (동료와 같은 속도예요)''', font = ('맑은 고딕', 8), fg = '#1a6b1a', justify = 'left', wraplength = 340).pack(anchor = 'w', pady = (0, 4))
    
        def _do_evolve_custom_body():
            '''PikaPet'''
            if not None('PikaPet', '정말 진화시킬까요? (되돌릴 수 없어요)'):
                return None
            if messagebox.askyesno.evolve_custom_body():
                None()
                return None
            None('PikaPet', '아직 진화 조건을 채우지 못했어요.')

        None(parent, text = '진화!', state = tk.NORMAL if cstatus.get('ready') else tk.DISABLED, command = _do_evolve_custom_body).pack(anchor = 'w', pady = (0, 4))
        return None
    party = (lambda .0: for x in .0:
    int(x).0)(self.state.get('party', [])())
    if int(d) in party:
        None(parent, text = f'''레벨: {self.companion_level_progress_text(d)}''', font = ('맑은 고딕', 8), fg = '#3a5a9a', justify = 'left', wraplength = 340).pack(anchor = 'w', pady = (0, 4))
        cstatus = self.companion_evolution_status(d)
        if not cstatus.get('evolvable'):
            None(parent, text = f'''🤝 장착된 동료예요. {cstatus.get('reason', '')}''', font = ('맑은 고딕', 8), fg = '#888', wraplength = 340, justify = 'left').pack(anchor = 'w')
            return None
        if tk.Label.get('is_eevee'):
            sp = SPECIES['eevee']
            None(parent, text = f'''🤝 장착된 동료 이브이예요.\n진행도: {min(cstatus['elapsed_days'], cstatus['days_needed']):.1f} / {cstatus['days_needed']:.1f}일  (본체와 같은 속도예요)''', font = ('맑은 고딕', 8), fg = '#1a6b1a', justify = 'left', wraplength = 340).pack(anchor = 'w', pady = (0, 4))
        
            def _do_evolve_companion_eevee(branch, branch_kr, dd = d):
                '''ready'''
                if not cstatus.get('ready'):
                    None('PikaPet', '아직 진화 조건을 채우지 못했어요.')
                    return None
                if not None('PikaPet', f'''정말 {branch_kr}(으)로 진화시킬까요?\n(진화 후에는 되돌릴 수 없어요)'''):
                    return None
                if None.askyesno.evolve_companion(dd, forced_branch = branch):
                    None()
                    return None
                None('PikaPet', '아직 진화 조건을 채우지 못했어요.')

            if eevee_friendship_ready(self.state):
                hour = None().tm_hour
                None(parent, text = f'''💞 친밀도 조건 달성! (애정도 {self.state.get('affection', 50):.0f} / {EEVEE_FRIENDSHIP_AFFECTION_MIN}, 불물전기 훈련 안 치우침) 에스피언·블래키 중 골라 진화할 수 있어요.''', font = ('맑은 고딕', 8), fg = '#a83a8a', justify = 'left', wraplength = 340).pack(anchor = 'w', pady = (4, 2))
                None(parent) = tk.Frame
                row.pack(anchor = 'w', pady = (0, 4))
                if cstatus.get('ready'):
                    cstatus.get('ready')
                e_ok = is_day
                if cstatus.get('ready'):
                    cstatus.get('ready')
                u_ok = not is_day
                None(row, text = '☀ 에스피언으로 진화!', state = tk.NORMAL if e_ok else tk.DISABLED, command = (lambda : None('psychic', '에스피언'))).pack(side = 'left', padx = (0, 4))
                None(row, text = '🌙 블래키로 진화!', state = tk.NORMAL if u_ok else tk.DISABLED, command = (lambda : None('dark', '블래키'))).pack(side = 'left')
                None(parent, text = '(낮이라 에스피언만 가능해요. 밤에 다시 와보세요.)' if is_day else '(밤이라 블래키만 가능해요. 낮에 다시 와보세요.)', font = ('맑은 고딕', 7), fg = '#888').pack(anchor = 'w')
                return None
            et = tk.Label.state.get('element_train', {
                'electric': 0,
                'water': 0,
                'fire': 0 })
            self._predict_eevee_branch() = tk.Label if tied else tk.Label
            predicted_kr = sp['branches'][predicted]['kr']
            None(parent, text = f'''지금 진화하면 예상: {predicted_kr} (원소 훈련 기준)''', font = ('맑은 고딕', 8), fg = '#555').pack(anchor = 'w', pady = (4, 2))
            None(parent, text = '진화!', state = tk.NORMAL if cstatus.get('ready') else tk.DISABLED, command = (lambda p = predicted, pk = predicted_kr: None(p, pk))).pack(anchor = 'w', pady = (2, 4))
            return None
        nxt = None['next_entry']
        None(parent, text = f'''🤝 장착된 동료예요. 다음 진화: {nxt.get('kr', '?')}\n진행도: {min(cstatus['elapsed_days'], cstatus['days_needed']):.1f} / {cstatus['days_needed']:.1f}일  (본체와 같은 속도예요)''', font = ('맑은 고딕', 8), fg = '#1a6b1a', justify = 'left', wraplength = 340).pack(anchor = 'w', pady = (0, 4))
    
        def _do_evolve_companion(dd = d):
            '''PikaPet'''
            if not None('PikaPet', f'''정말 {POKEDEX.get(dd, { }).get('kr', '?')}을(를) 진화시킬까요?'''):
                return None
            if messagebox.askyesno.evolve_companion(dd):
                None()
                return None
            None('PikaPet', '아직 진화 조건을 채우지 못했어요.')

        None(parent, text = '진화!', state = tk.NORMAL if cstatus.get('ready') else tk.DISABLED, command = _do_evolve_companion).pack(anchor = 'w', pady = (0, 4))
        return None
    if not None:
        None(parent, text = '아직 만나지 못한 포켓몬이에요.', font = ('맑은 고딕', 8), fg = '#888').pack(anchor = 'w')
        return None
    entry_chain_len = None.get('chain_len', 1)
    entry_stage = entry.get('stage', 0)
    if d == EEVEE_BASE_DEX:
        None(parent, text = '이 포켓몬을 동료로 장착하면 진화 타이머가 시작되고, 본체와 똑같이\n부스터/샤미드/쥬피썬더/에스피언/블래키 갈래를 직접 골라 진화시킬 수 있어요.', font = ('맑은 고딕', 8), fg = '#888', justify = 'left', wraplength = 340).pack(anchor = 'w')
        return None
    if None in EEVEE_DEX_SET:
        None(parent, text = '이미 최종 진화 단계예요.', font = ('맑은 고딕', 8), fg = '#888').pack(anchor = 'w')
        return None
    if None < 2 or entry_stage >= entry_chain_len - 1:
        None(parent, text = '이미 최종 진화 단계이거나, 원래 진화하지 않는 종이에요.', font = ('맑은 고딕', 8), fg = '#888').pack(anchor = 'w')
        return None
    if None in COMPANION_EVOLVE_EXCLUDE:
        None(parent, text = '갈래가 여러 개로 나뉘는 종이라 동료 자동진화 대상이 아니에요.', font = ('맑은 고딕', 8), fg = '#888').pack(anchor = 'w')
        return None
    None(parent, text = '이 포켓몬을 동료로 장착하면 진화 타이머가 시작돼요.\n(도감 탭 → 하단 장착 칸에서 장착할 수 있어요)', font = ('맑은 고딕', 8), fg = '#888', justify = 'left', wraplength = 340).pack(anchor = 'w')
