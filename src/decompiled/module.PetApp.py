# module.PetApp
# source line 4515
# Recovered from bytecode; default argument values are not shown.

def PetApp():
    __firstlineno__ = 4515
    __classdict__ = <NODE:36>

    def __init__(self, root, state):
        global _APP_INSTANCE
        _APP_INSTANCE = self
        self.root = root
        self.state = state
        self.restart_requested = False
        for None in DEFAULT_STATE.items():
            k = ()
            v = None
            if not k not in self.state:
                continue
            if not isinstance(v, (list, dict)):
                pass
            elif isinstance(v, list):
                pass
        
        list(v)
        for None in (('element_train', DEFAULT_STATE['element_train']), ('daily_action_count', DEFAULT_STATE['daily_action_count']), ('train_sessions', DEFAULT_STATE['train_sessions']), ('catch_counts', DEFAULT_STATE['catch_counts']), ('minigame_daily', DEFAULT_STATE['minigame_daily']), ('dex', { }), ('caught', { }), ('missed', { }), ('companion_evolve_started', { })):
            key = ()
            default_val = None
            if isinstance(self.state.get(key), dict):
                continue
        (('element_train', DEFAULT_STATE['element_train']), ('daily_action_count', DEFAULT_STATE['daily_action_count']), ('train_sessions', DEFAULT_STATE['train_sessions']), ('catch_counts', DEFAULT_STATE['catch_counts']), ('minigame_daily', DEFAULT_STATE['minigame_daily']), ('dex', { }), ('caught', { }), ('missed', { }), ('companion_evolve_started', { }))
        if not isinstance(self.state.get('party'), list):
            [] = v
        ensure_catch_counts(self.state)
        if not self.state.get('stage_started_at'):
            self.state['stage_started_at'] = None()
        (self.screen_left, self.screen_top, self.screen_w, self.screen_h) = self._compute_screen_rect()
        self.taskbar_rect = None
    
        try:
            self.taskbar_rect = None()
            self._fx_kind = None
            self._fx_started_at = 0
            self._fx_duration = 0
            self._fx_toast_win = None
            self._omok_open = False
            self._mine_run = None
            ids = get_all_stage_ids(self.state['starter'])
            self.anim_sets = { }
            for sid in ids:
                self.anim_sets[sid] = None(sprite_folder_path(sid))
            ids
            self._mega_anim_sets = { }
            if self.state.get('custom_body_dex'):
                self._ensure_body_anim_loaded(self.state['custom_body_dex'])
            self.direction = spriteanim.DIR_DOWN
            self.walk_facing_dir = spriteanim.DIR_RIGHT
            self.pos_x = self.screen_left + self.screen_w // 2
            self.pos_y = self._get_floor_y()
            self.ground_mode = 'floor'
            self.ground_left = self.screen_left
            self.ground_right = self.screen_left + self.screen_w
            self.behavior_state = 'idle'
            self._fall_vel = 0
            self._kb_jumps_used = 0
            self._kb_jump_active = False
            self._kb_double_jumped = False
            self._walk_target_x = self.pos_x
            self._walk_target_y = self.pos_y
            self._walk_on_arrive = None
            self.idle_next_decision_at = 0
            self._sleep_until = 0
            self._sleep_started_at = 0
            self._corner_sleep = False
            self._hide_timer_id = None
            self._ledges_cache = []
            self._ledges_cache_at = 0
            self._icons_cache = []
            self._icons_cache_at = 0
            self._last_hover_react = 0
            self._last_save = 0
            self._last_companion_evo_check = 0
            self._last_screen_check = 0
            self._last_topmost_reassert = 0
            self._last_tick_error_msg = None
            self._last_tick_error_log_at = 0
            self._last_encounter_at = 0
            self.battle_open = False
            self._battle_win = None
            self._battle_ctx = None
            self._battle_minimized = False
            self._pending_encounter = None
            self._encounter_toast_win = None
            self._train_done_toast_win = None
            self._train_done_notified_at = None
            self._food_done_toast_win = None
            self._food_boost_notified_until = 0
            self._blink_job = None
            self._blink_state = False
            self._taskbar_alert_job = None
            self._press_x_root = 0
            self._press_y_root = 0
            self._press_widget_x = 0
            self._press_widget_y = 0
            self._press_dragging = False
            self.current_action = 'Idle'
            self.current_logical = None
            self.current_frame_idx = 0
            self._frame_elapsed = 0
            self._anim_loop = True
            self._anim_on_complete = None
            self._img_w = 60
            self._img_h = 60
            self._tkimg = None
            self.label = None(root, bd = 0, bg = MAGIC)
            self.label.pack()
            self.label.bind('<ButtonPress-1>', self.on_press)
            self.label.bind('<B1-Motion>', self.on_motion)
            self.label.bind('<ButtonRelease-1>', self.on_release)
            self.label.bind('<Button-3>', (lambda e: self.build_menu()))
            self.label.bind('<Enter>', self.on_hover)
            self._key_left = False
            self._key_right = False
            self._key_up = False
            self._key_down = False
            self._space_held = False
        
            def _space_press(e):
                if self._space_held:
                    return None
                self._space_held = None
                self.kb_jump()

        
            def _space_release(e):
                self._space_held = False

            for None in (('<KeyPress-Left>', (lambda e: setattr(self, '_key_left', True))), ('<KeyRelease-Left>', (lambda e: setattr(self, '_key_left', False))), ('<KeyPress-Right>', (lambda e: setattr(self, '_key_right', True))), ('<KeyRelease-Right>', (lambda e: setattr(self, '_key_right', False))), ('<KeyPress-Up>', (lambda e: setattr(self, '_key_up', True))), ('<KeyRelease-Up>', (lambda e: setattr(self, '_key_up', False))), ('<KeyPress-Down>', (lambda e: setattr(self, '_key_down', True))), ('<KeyRelease-Down>', (lambda e: setattr(self, '_key_down', False))), ('<KeyPress-space>', _space_press), ('<KeyRelease-space>', _space_release)):
                seq = ()
                fn = None
                self.root.bind_all(seq, fn, add = '+')
            tk.Label
            None = None
            self.setup_tray()
            self._taskbar_win = None
            self._setup_taskbar_icon()
            self._pvp_lobby_win = None
            self._pvp_history_win = None
            self._pvp_help_win = None
            self._record_login_day()
        
            try:
                _startup_title_msgs = self._check_new_titles()
                if _startup_title_msgs:
                
                    try:
                        self.root.after(3000, (lambda : self._popup_title_msgs(_startup_title_msgs)))
                        self.companions = []
                        self.body2 = None
                        self._rebuild_companions()
                        self._last_duo_trick = None()
                        if self.state.get('in_ball'):
                        
                            try:
                                self.root.withdraw()
                            self.redraw()
                            self._apply_body1_visibility()
                            self._last_tick = None()
                            self.root.after(TICK_MS, self.tick)
                            return None
                            except Exception:
                                time.time
                                self.taskbar_rect = None
                                continue

                            except Exception:
                                time.time
                                continue
                            except Exception:
                                time.time
                                continue
                            except Exception:
                                time.time
                                continue
                            except Exception:
                                time.time
                                continue





    def stage_conf(self):
        '''화면에 실제로 보여줄 본체 정보 (본체 교체 중이면 그 포켓몬 기준).'''
        return display_stage_conf_for(self.state)


    def starter_stage_conf(self):
        '''진화 로직/진화 탭 전용: 본체 교체와 무관하게 항상 원래 스타터의 진행 상황만 본다.'''
        return stage_conf_for(self.state)


    def body_display_scale(self):
        """본체(화면에 보이는 크기)의 실제 배율. 레벨이 아니라 '진화 단계'로 정한다 -
    갓 진화했는데 레벨이 낮아서 작게 보이거나, 반대로 레벨만 높고 아직 진화 전이라
    어색하게 커 보이는 걸 막기 위함. 남은 진화 단계가 없으면(최종형) 가장 크게,
    한 단계 남았으면 중간, 아직 많이 남았으면(기본형) 종족 고유 크기 그대로."""
        base_scale = self.stage_conf().get('scale', 0.6)
        remaining = self.starter_remaining_stages()
        if remaining <= 0:
            bonus = 0.45
            return base_scale + bonus
        if None == 1:
            bonus = 0.22
            return base_scale + bonus
        bonus = None
        return base_scale + bonus


    def _ensure_body_anim_loaded(self, dex):
        '''본체 교체용 스프라이트를 self.anim_sets 캐시에 없으면 새로 불러온다.'''
        key = f'''pdx_{dex}'''
        if key in self.anim_sets:
            return None
        entry = None.get(int(dex))
        if not entry:
            return None
    
        try:
            self.anim_sets[key] = None(sprite_folder_path(entry['en']))
            return None
        except Exception:
            return None



    def _dex_is_taken_by_body(self, d):
        '''이 도감번호가 지금 1번 본체(본체 교체) 또는 2번 본체로 이미 쓰이고 있는지.
    본체 역할과 동료 역할을 동시에 주면 능력치가 중복 적용되므로, 동료로 새로
    장착하려는 곳마다 이 함수로 먼저 막는다.'''
    
        try:
            d = int(d)
            if not self.state.get('custom_body_dex'):
                self.state.get('custom_body_dex')
            if d == int(-1):
                return True
            dex2 = None(self.state)
            if dex2 is not None and d == int(dex2):
                return True
            return None
        except Exception:
            return False



    def _remove_dex_from_companion_slots(self, dex):
        '''이 도감번호를 기본 세팅(party)과 상황별 프리셋(체육관/코드대결/로켓단습격/
    무한성장 각 모드) 전부에서 빼준다. 본체나 2번 본체로 새로 장착된 종이 동시에
    동료로도 남아있으면 능력치(본체 효과 + 동료 시너지)가 중복 적용되기 때문에,
    본체 쪽으로 넣을 때마다 이 함수로 정리한다. 뭔가 바뀌었으면 True를 돌려준다.'''
        dex = int(dex)
        changed = False
        for None in party_now,:
            if not int(d) != dex:
                continue
        party_now, = , []
        d = self.state.get('party', []), d
        if len(party_now) != len(self.state.get('party', [])):
            self.state['party'] = party_now
            changed = True
        presets = self.state.setdefault('battle_presets', { })
        for _cat in PRESET_CATEGORIES:
            _slots = list(presets.get(_cat, []))
            for None in :
                s = None
        
            , [], _new_slots, s = _slots, s
            if not _new_slots != _slots:
                continue
            presets[_cat] = _new_slots
        for None in mega_party_now,:
            if not int(d) != dex:
                continue
        mega_party_now, = , []
        d = self.state.get('mega_party', []), d
        if len(mega_party_now) != len(self.state.get('mega_party', [])):
            self.state['mega_party'] = mega_party_now
        if changed:
        
            try:
                self._rebuild_companions()
                return changed
                return changed
            
            
            
            except Exception:
                return changed



    def set_custom_body(self, dex):
        '''본체를 다른(잡은) 포켓몬으로 교체한다. dex=None이면 원래 스타터로 되돌린다.
    도감 목록에서 "↩ 스타터로 되돌리기" 버튼을 안 쓰고, 위쪽에 고정 표시된
    "🌟 스타터" 항목을 직접 선택해서 "🏠 본체로 교체"를 눌러도 결과가 똑같아야
    한다. 그런데 스타터 종은 원래 caught 딕셔너리에 기록이 없이(player_level()을
    직접 쓰는 방식으로) 따로 관리되기 때문에, 그대로 custom_body_dex에 스타터의
    도감번호를 넣어버리면 body1_effective_level()이 caught 기록을 못 찾아
    레벨을 1로 잘못 보여주는 버그가 있었다. 그래서 스타터 자신의 도감번호가
    들어오면 그냥 되돌리기(None)와 똑같이 처리한다.'''
        if dex is not None:
        
            try:
                pinned_dex = self.starter_stage_conf().get('dex')
                if pinned_dex is not None and int(dex) == int(pinned_dex):
                    dex = None
                if dex is None:
                    self.state['custom_body_dex'] = None
                else:
                    dex = int(dex)
                    self._ensure_body_anim_loaded(dex)
                    self.state['custom_body_dex'] = dex
                    self._remove_dex_from_companion_slots(dex)
                self.save_state()
                self._finish_to_idle()
                self.redraw()
            
                try:
                    if self.tray_icon:
                    
                        try:
                            self.tray_icon.icon = self._tray_image()
                            return None
                            return None
                            except Exception:
                                pinned_dex = None
                                continue
                        except Exception:
                            return None





    def current_element(self):
        '''element'''
        conf = self.stage_conf()
        if not conf.get('element'):
            conf.get('element')
        return SPECIES[self.state['starter']].get('element', 'normal')


    def companion_type_bonus_pct(self, defender_types):
        '''지금 장착된 동료들이 defender_types(상대 타입)에게 상성상 유리할 때 더해줄 %p.'''
        equipped_party = list(self.state.get('party', []))[:companion_slot_count(self.state)]
        return companion_type_synergy_pct(equipped_party, defender_types)


    def my_type_effect_mult(self, defender_types):
        '''내 본체 상성 배율 + 장착 동료들의 상성 시너지 보너스(%p)까지 합친 최종 배율.'''
        base = type_effect_multiplier(self.current_element(), defender_types)
        return base + self.companion_type_bonus_pct(defender_types) / 100


    def is_eevee_base(self):
        '''custom_body_dex'''
        if not self.state.get('custom_body_dex'):
            not self.state.get('custom_body_dex')
            if self.state.get('starter') == 'eevee':
                self.state.get('starter') == 'eevee'
        return self.state.get('stage', 0) == 0


    def resolve(self, logical):
        '''happy'''
        val = self.stage_conf().get(logical)
        if val:
            return val
        if None == 'happy':
            return self._pick_dynamic_action(HAPPY_ACTION_CANDIDATES)
        if None == 'hungry':
            return self._pick_dynamic_action(HUNGRY_ACTION_CANDIDATES)


    def _pick_dynamic_action(self, candidates):
        '''SPECIES에 따로 지정된 값이 없는 로지컬 동작(친밀도/배고픔 리액션 등)을 위해,
    지금 스프라이트에 실제로 있는 동작을 후보 목록 순서대로 찾아서 돌려준다.
    하나도 없으면 None (그러면 _do_one_shot이 그냥 조용히 넘어간다).'''
        aset = self.anim_sets.get(self.stage_conf()['id'])
        if aset is None:
            return None
        for name in None:
            if aset.has(name):
                if aset.n_frames(name) > 0:
                
                    return None, name
        return None
        except Exception:
            continue


    def save_state(self):
        save_state_to_disk(self.state)


    def manual_save_now(self):
        """우클릭 메뉴의 '지금 저장하기' 버튼. 자동저장은 이미 계속 되고 있지만, 사용자가
    직접 눌러서 '지금 이 순간 확실하게 저장됐다'는 걸 눈으로 확인하고 안심할 수 있게
    하기 위한 기능. 저장 직후 파일을 다시 읽어 확인까지 하고, 성공/실패를 팝업으로 알려준다."""
        ok = save_state_to_disk(self.state)
        if ok:
            None('저장 완료', f'''✅ 지금 상태가 확실하게 저장됐어요!\n컴퓨터를 끄거나 프로그램을 종료한 뒤 다시 켜도 이 상태 그대로 이어져요.\n\n저장 위치: {STATE_PATH}''')
            return None
        None('저장 실패 - 확인해주세요', f'''⚠ 저장이 안 됐어요! 아래를 확인해주세요.\n\n예상되는 원인:\n· 윈도우 보안 > 바이러스 및 위협 방지 > \'랜섬웨어 방지\'의\n   \'제어된 폴더 접근\'이 이 프로그램의 파일 쓰기를 막고 있을 수 있어요\n   (꺼주시거나, 이 프로그램을 허용 앱 목록에 추가해주세요)\n· 백신 프로그램이 저장을 차단하고 있을 수 있어요\n\n저장 위치: {STATE_PATH}\n이 폴더에 이 프로그램이 파일을 쓸 수 있는지 확인해주세요.''')


    def _get_floor_y(self):
        fallback = self.screen_top + self.screen_h - GROUND_MARGIN
        if self.taskbar_rect:
            floor_y = self.taskbar_rect[1]
            if floor_y < self.screen_top + self.screen_h * 0.5:
                return fallback
            if None > None.screen_top + self.screen_h + 200:
                return fallback
            return None


    def _compute_screen_rect(self):
        '''지금 설정(듀얼모니터 "기존 설정" vs "주 모니터만 사용" vs "보조 모니터만 사용")에
    맞는 화면 범위를 계산한다. 게임 안의 모든 창 배치(야생 포켓몬 조우, 레벨업/진화 알림,
    펫 이동 범위 등)가 전부 self.screen_left/top/w/h 이 4개 값만 기준으로 삼기 때문에,
    여기 한 곳만 설정에 맞춰 값을 바꿔주면 나머지 코드는 손댈 필요가 없다.'''
        if self.state.get('secondary_monitor_mode'):
        
            try:
                rect = None()
                if rect:
                    return rect
                if winlayer.get_secondary_monitor_rect.state.get('single_monitor_mode') or self.state.get('secondary_monitor_mode'):
                
                    try:
                        w = self.root.winfo_screenwidth()
                        h = self.root.winfo_screenheight()
                        return (0, 0, max(1, w), max(1, h))
                    
                        try:
                            vrect = None()
                            if vrect:
                                return vrect
                        
                            try:
                                w = self.root.winfo_screenwidth()
                                h = self.root.winfo_screenheight()
                                return (0, 0, max(1, w), max(1, h))
                                except Exception:
                                    rect = None
                                    continue
                                except Exception:
                                    h = 720
                                    w = 1280
                                    continue
                                except Exception:
                                    vrect = None
                                    continue
                            except Exception:
                                h = 720
                                w = 1280
                                continue






    def _rocket_screen_rect(self):
        '''로켓단 습격 창(토스트/미리보기)을 띄울 화면 범위. 평소 펫 이동범위(self.screen_*)와
    설정에서 별도로 "주 모니터"/"보조 모니터"를 고르면 그쪽을 우선한다. "아무데나"거나
    설정을 못 찾으면 지금 펫이 쓰는 범위(self.screen_*)를 그대로 쓴다.'''
        loc = self.state.get('rocket_ambush_location', 'any')
        if loc == 'main':
        
            try:
                w = self.root.winfo_screenwidth()
                h = self.root.winfo_screenheight()
                return (0, 0, max(1, w), max(1, h))
                if loc == 'secondary':
                
                    try:
                        rect = None()
                        if rect:
                            return rect
                        return (winlayer.get_secondary_monitor_rect.screen_left, self.screen_top, self.screen_w, self.screen_h)
                        except Exception:
                            continue
                    except Exception:
                        rect = None
                        continue




    def set_single_monitor_mode(self, on):
        '''설정 메뉴에서 "주 모니터만 사용"을 켤 때 호출. "보조 모니터만 사용"과는 동시에
    켤 수 없어서(라디오 버튼) 서로 꺼준다. 전환 즉시 화면 범위를 다시 계산하고, 지금
    펫이 새 범위 밖에 있으면 안전하게 데려온다(주 모니터 중앙으로).'''
        self.state['single_monitor_mode'] = bool(on)
        if on:
            self.state['secondary_monitor_mode'] = False
        self.save_state()
        self._refresh_screen_bounds(force = True)
        left = ()
        top = (self.screen_left, self.screen_top, self.screen_w, self.screen_h)
        w = None
        h = None
        if  <= left, self.pos_x or left, self.pos_x <= left + w:
            pass
    
        if not  <= top, self.pos_y or top, self.pos_y <= top + h:
            pass
    
        self.force_recall_primary_center()
        return None


    def set_secondary_monitor_mode(self, on):
        '''설정 메뉴에서 "보조 모니터만 사용"을 켤 때 호출. 모니터가 하나뿐이면
    _compute_screen_rect()가 자동으로 주 모니터로 대신 계산한다.'''
        self.state['secondary_monitor_mode'] = bool(on)
        if on:
            self.state['single_monitor_mode'] = False
        self.save_state()
        self._refresh_screen_bounds(force = True)
        left = ()
        top = (self.screen_left, self.screen_top, self.screen_w, self.screen_h)
        w = None
        h = None
        if  <= left, self.pos_x or left, self.pos_x <= left + w:
            pass
    
        if not  <= top, self.pos_y or top, self.pos_y <= top + h:
            pass
    
        self.force_recall_to(left + w // 2, top + h // 2)
        return None


    def _refresh_screen_bounds(self, force = False):
        '''모니터 구성(듀얼모니터를 뺐다 꼈다, 해상도 변경, 도킹/언도킹 등)이 바뀌었는지
    주기적으로 다시 확인해서 화면 범위를 최신 상태로 맞춘다.
    예전에는 프로그램을 켤 때 딱 한 번만 화면 크기를 재서, 그 뒤로 모니터 구성이
    바뀌면(특히 두 번째 모니터가 꺼지거나 연결이 끊기면) 포켓몬이 이제는 없는
    모니터 자리에 낀 채로 "사라진 것처럼" 안 돌아오는 문제가 있었다.'''
        left = ()
        top = self._compute_screen_rect()
        w = None
        h = None
        if w <= 0 or h <= 0:
            return None
        if not None and left != self.screen_left:
            left != self.screen_left
            if not top != self.screen_top:
                top != self.screen_top
                if not w != self.screen_w:
                    w != self.screen_w
        (self.screen_left, self.screen_top, self.screen_w, self.screen_h) = (left, top, w, h)
    
        try:
            self.taskbar_rect = None()
            if changed:
                self._clamp_to_screen()
                return None
            return winlayer.get_taskbar_rect
        except Exception:
            continue



    def _clamp_to_screen(self):
        '''지금 위치가 (모니터 구성이 바뀌는 등의 이유로) 화면 밖으로 나가 있으면
    안전하게 화면 안으로 되돌린다. 몬스터볼 안에 있을 때는 어차피 안 보이니 건드리지 않는다.'''
        if self.state.get('in_ball'):
            return None
        if not None.behavior_state in ('held', 'climb'):
            None.behavior_state in ('held', 'climb')
            if not self._press_dragging:
                self._press_dragging
        actively_controlled = self.state.get('keyboard_control')
        margin = 20
        min_x = self.screen_left + margin
        max_x = self.screen_left + self.screen_w - margin
        if max_x < min_x:
            max_x = min_x
        if not actively_controlled and out_of_bounds:
            return None
        not None if  <= self.screen_left, self.pos_x else None, self.screen_left, self.pos_x <= self.screen_left + self.screen_w(min_x, min(max_x, self.pos_x)) = None
        self.ground_left = self.screen_left
        self.ground_right = self.screen_left + self.screen_w
        if self.ground_mode == 'floor' or out_of_bounds:
            self.pos_y = self._get_floor_y()
        self._walk_target_x = self.pos_x
        self._walk_target_y = self.pos_y
        if out_of_bounds:
            self._press_dragging = False
            self._fall_vel = 0
            self.ground_mode = 'floor'
            self.behavior_state = 'idle'
        
            try:
                self.enter_idle()
            
                try:
                    self.redraw()
                
                    try:
                        if self.tray_icon:
                        
                            try:
                                self.tray_icon.notify('모니터 구성이 바뀌어서 포켓몬을 화면 안으로 다시 데려왔어요.', 'PikaPet')
                                return None
                                return None
                                return None
                                except Exception:
                                    continue
                                except Exception:
                                    continue
                            except Exception:
                                return None






    def _weight_factor(self):
        '''weight'''
        w = self.state.get('weight', 50)
        return 0.9 + 0.2 * (w / 100)


    def player_level(self):
        return player_level_from_state(self.state)


    def starter_remaining_stages(self):
