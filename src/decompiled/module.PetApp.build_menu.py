# module.PetApp.build_menu
# source line 18212
# Recovered from bytecode; default argument values are not shown.

def build_menu(self):
    self._wake_from_corner_sleep()
    m = None(self.root, tearoff = 0)
    if self._pending_encounter:
        if len(self._pending_encounter) > 4:
            len(self._pending_encounter) > 4
        pe_is_shiny = self._pending_encounter[4]
        pe_label = '✨ 이로치다! 얼른 확인하기!' if pe_is_shiny else '⚡ 야생 포켓몬 확인하기!'
        m.add_command(label = pe_label, command = self._open_pending_encounter)
        m.add_separator()
    if self._battle_minimized:
        m.add_command(label = '⚔ 전투 창 다시 열기', command = self._restore_battle_window)
        m.add_separator()
    skill_kr = TYPE_SKILL_LABEL.get(self.current_element(), '스킬')
    m.add_command(label = f'''✨ {skill_kr}''', command = self.use_skill)
    m.add_command(label = '🎉 재주부리기', command = self.trick)
    m.add_command(label = '🌙 재우기', command = self.sleep_now)
    m.add_command(label = '😴 구석에서 잠자기', command = self.sleep_in_corner)
    if self.is_eevee_base():
        m.add_separator()
        et = self.state.get('element_train', { })
        m.add_command(label = f'''🔥 불 속성 훈련 ({et.get('fire', 0)})''', command = (lambda : self.train_element('fire')))
        m.add_command(label = f'''💧 물 속성 훈련 ({et.get('water', 0)})''', command = (lambda : self.train_element('water')))
        m.add_command(label = f'''⚡ 번개 속성 훈련 ({et.get('electric', 0)})''', command = (lambda : self.train_element('electric')))
    m.add_separator()
    _cur_scale = self.state.get('manual_scale', 1)
    _cur_size_label = (lambda .0: for None in .0:
    lb = ()v = Noneif not abs(v - _cur_scale) < 0.001:
    continuelb)(SIZE_OPTIONS(), f'''{_cur_scale:.2f}배''')
    size_menu = None(m, tearoff = 0)
    size_var = None(value = _cur_scale)
    for None in SIZE_OPTIONS:
        label = ()
        val = None
    tk.DoubleVar
    m.add_cascade(label = f'''📏 크기 조절 (지금: {_cur_size_label})''', menu = size_menu)
    m.add_command(label = '📖 도감 보기 / 동료 장착', command = self.open_pokedex)
    m.add_command(label = evo_label, command = self.open_evolution_tab)
    None(m, tearoff = 0) = tk.Menu
    daily_menu.add_command(label = '📋 오늘 진행 상황 보기', command = self._show_daily_quest_overview)
    daily_menu.add_separator()
    daily_menu.add_command(label = '🍎 먹이 주기', command = self.feed)
    daily_menu.add_command(label = '🏃 운동시키기', command = self.exercise)
    daily_menu.add_command(label = '🤗 쓰다듬기', command = self.pet_interact)
    daily_menu.add_separator()
    daily_menu.add_command(label = '🎁 도형님이 주는 선물', command = self.open_daily_gift)
    mine_left = MINE_MAX_PER_DAY - self._mine_today_count()
    mine_label = f'''⛏ 광산 ({mine_left}/{MINE_MAX_PER_DAY}회 남음)''' if mine_left > 0 else '⛏ 광산 (오늘 다 씀)'
    daily_menu.add_command(label = mine_label, command = self.open_mining)
    gacha_left = GACHA_MAX_PER_DAY - self._gacha_today_count()
    gacha_label = f'''🎰 코인뽑기 ({gacha_left}/{GACHA_MAX_PER_DAY}회 남음)''' if gacha_left > 0 else '🎰 코인뽑기 (오늘 다 씀)'
    daily_menu.add_command(label = gacha_label, command = self.open_coin_gacha)
    daily_menu.add_command(label = '🏋 수련의 방', command = self.open_training_room)
    daily_menu.add_command(label = '⛏ 무한의 돌', command = self.open_infinite_stone)
    daily_menu.add_command(label = '🎮 미니게임', command = self.open_minigame_hub)
    m.add_cascade(label = '📅 일일퀘스트', menu = daily_menu)
    if self.state.get('mega_evolved') and self.mega_ready() or is_final_stage(self.state):
        m.add_command(label = '💎 메가진화', command = self.open_mega_evolve)
    kb_on = self.state.get('keyboard_control')
    m.add_command(label = '🎮 방향키 조작 끄기 (지금 켜짐)' if kb_on else '🎮 방향키 조작 켜기 (←/→ 이동, 스페이스 점프)', command = self.toggle_keyboard_control)
    recall_menu = None(m, tearoff = 0)
    recall_menu.add_command(label = '화면 중앙으로', command = self.force_recall)
    recall_menu.add_command(label = '마우스 위치로', command = self.force_recall_to_cursor)
    recall_menu.add_command(label = '화면 왼쪽 위 구석으로', command = self.force_recall_top_left)
    recall_menu.add_command(label = '주 모니터 중앙으로', command = self.force_recall_primary_center)
    m.add_cascade(label = '📍 불러오기 (위치 선택)', menu = recall_menu)
    m.add_command(label = '🔴 몬스터볼로 들어가기', command = self.enter_ball)
    m.add_command(label = '🕒 시계 / 할일', command = self.open_todo)
    m.add_command(label = '📊 상태 보기', command = self.open_status)
    m.add_command(label = '🏆 칭호 보기', command = self.open_titles_view)
    m.add_command(label = '📈 내 스탯 자세히 보기', command = self.open_stat_detail)
    m.add_command(label = '🔑 코드 대결', command = self.open_battle_code)
    m.add_command(label = '🏅 체육관', command = self.open_gym_hub)
    m.add_command(label = f'''🏪 상점 (💰{self.state.get('gold', 0)}골드)''', command = self.open_shop)
    inf_unlocked = genN_gym_badges_complete(self.state, 1)
    inf_label = '♾ 무한성장미터' if inf_unlocked else '♾ 무한성장미터 (🔒1세대 뱃지 필요)'
    m.add_command(label = inf_label, command = self.open_infinite_meter_hub)
    m.add_command(label = '⚙ 설정', command = self.open_settings)
    m.add_separator()
    m.add_command(label = '💾 지금 저장하기 (100% 확실하게)', command = self.manual_save_now)
    m.add_command(label = '🔆 창 투명도 복구', command = self._restore_window_opacity)
    m.add_command(label = '❌ 종료', command = self.quit_app)

    try:
        m.tk_popup(self.root.winfo_pointerx(), self.root.winfo_pointery())
    
        try:
            m.grab_release()
            return None
        except Exception:
            '🧬 진화/레벨 탭 ✨진화가능!' if self.evolution_ready() else '🧬 진화/레벨 탭'
            return None
            m.grab_release()
            except Exception:
                tk.Menu
