# module.PetApp.__init__
# source line 4516
# Recovered from bytecode; default argument values are not shown.

def __init__(self, root, state):
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
