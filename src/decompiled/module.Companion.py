# module.Companion
# source line 4099
# Recovered from bytecode; default argument values are not shown.

def Companion():
    __firstlineno__ = 4099
    __classdict__ = <NODE:36>

    def __init__(self, owner, dex, level, slot_index = 0, mega = False, is_body2 = False):
        self.owner = owner
        self.dex = dex
        self.level = level
        self.slot_index = slot_index
        self.entry = POKEDEX.get(dex)
        self.mega = bool(mega)
        self.is_body2 = bool(is_body2)
        self.anim_set = None
        sprite_name = self.entry['en'] if self.entry else None
        if self.mega and self.entry:
            mega_folder = companion_mega_sprite_folder(self.entry)
            if mega_folder:
                sprite_name = mega_folder
        if sprite_name:
        
            try:
                self.anim_set = None(sprite_folder_path(sprite_name))
                self.action = self.entry['idle'] if self.entry else 'Idle'
                self.frame_idx = 0
                self._elapsed = 0
                self._tkimg = None
                self.direction = owner.direction
                self.free_x = None
                self.free_y = None
                self.free_state = 'idle'
                self._free_target_x = None
                self._free_next_decision_at = 0
                self._free_fallen_until = 0
                self._free_playing_until = 0
                self._synced_sleep = False
                self.win = None(owner.root)
                self.win.overrideredirect(True)
            
                try:
                    self.win.attributes('-topmost', True)
                
                    try:
                        self.win.attributes('-transparentcolor', MAGIC)
                        self.win.config(bg = MAGIC)
                        self.label = None(self.win, bd = 0, bg = MAGIC)
                        self.label.pack()
                        self._img_w = None
                        self._img_h = None
                        self._dragging = False
                        self._first_positioned = False
                    
                        try:
                            self.win.withdraw()
                            self.label.bind('<ButtonPress-1>', self.on_press)
                            self.label.bind('<B1-Motion>', self.on_motion)
                            self.label.bind('<ButtonRelease-1>', self.on_release)
                            self.label.bind('<Button-3>', self.on_right_click)
                            return None
                            except Exception:
                                tk.Toplevel
                                self.anim_set = None
                                continue
                            except Exception:
                                tk.Toplevel
                                continue
                            except Exception:
                                tk.Toplevel
                                continue
                        except Exception:
                            tk.Toplevel
                            continue






    def on_right_click(self, event):
        """본체2/동료(작은 아이콘) 우클릭 메뉴 - 예전엔 '⚙ 설정' 하나만 달랑 나와서, 도감/
    진화탭/상점/일일퀘스트 같은 기능을 쓰려면 매번 1번 본체까지 마우스를 옮겨야 했다.
    이제 1번 본체 우클릭과 완전히 똑같은 전체 메뉴(build_menu)를 그대로 띄워서,
    동료를 우클릭해도 본체를 우클릭한 것과 똑같이 모든 기능에 바로 접근할 수 있다."""
    
        try:
            self.owner.build_menu()
            return None
        except Exception:
            return None



    def on_press(self, event):
        """'자유롭게 배회' 모드에서만 동료를 마우스로 잡아서 옮길 수 있게 한다."""
        if self.owner.state.get('companion_layout', 'line') != 'free':
            return None
        self._press_x_root = None.x_root
        self._press_y_root = event.y_root
        self._press_widget_x = event.x
        self._press_widget_y = event.y
        self._dragging = False


    def on_motion(self, event):
        '''companion_layout'''
        if self.owner.state.get('companion_layout', 'line') != 'free':
            return None
        if not None(self, '_press_x_root'):
            return None
        dx = None.x_root - self._press_x_root
        dy = event.y_root - self._press_y_root
        if not self._dragging:
            if abs(dx) < DRAG_THRESHOLD_PX and abs(dy) < DRAG_THRESHOLD_PX:
                return None
            self._dragging = None
            self.free_state = 'idle'
            self.action = self.entry['idle'] if self.entry else 'Idle'
        new_left = event.x_root - self._press_widget_x
        new_top = event.y_root - self._press_widget_y
    
        try:
            self.win.geometry(f'''+{int(new_left)}+{int(new_top)}''')
            return None
        except Exception:
            return None



    def on_release(self, event):
        '''companion_layout'''
        if self.owner.state.get('companion_layout', 'line') != 'free':
            return None
        if None._dragging:
            if not self._img_w:
                self._img_w
            w = 40
            if not self._img_h:
                self._img_h
            h = 40
            left = event.x_root - self._press_widget_x
            top = event.y_root - self._press_widget_y
            self.free_x = left + w / 2
            self.free_y = top + h
            self._dragging = False
            self.free_state = 'idle'
            self._free_next_decision_at = random.uniform + None(1.5, 3)
            return None


    def step(self, dt_ms):
        if not self.anim_set or self.entry:
            return None
        layout = None.owner.state.get('companion_layout', 'line')
        if layout == 'free':
            if not self._dragging:
                self._step_free_roam(dt_ms)
            direction = self.direction if self.direction is not None else self.owner.direction
        elif self._synced_sleep and self.anim_set.has('Sleep'):
            self.action = 'Sleep'
        elif self.action == 'Sleep':
            self.action = self.entry['idle']
            self.frame_idx = 0
        direction = self.owner.direction
        self.anim_set.duration_of(self.action, self.frame_idx) * ANIM_TICK_MS = self, self._elapsed += dt_ms, ._elapsed
        if dur <= 0:
            dur = ANIM_TICK_MS
        if self._elapsed >= dur:
            self.anim_set.n_frames(self.action) = self, self._elapsed -= dur, ._elapsed
            if n > 0:
                self.frame_idx = (self.frame_idx + 1) % n
        frame = self.anim_set.frame(self.action, self.frame_idx, direction)
        if frame is None:
            return None
        scale = None(self.entry) * self.owner.state.get('manual_scale', 1) * sprite_extra_scale(self.dex)
        w = max(8, int(frame.width * scale))
        h = max(8, int(frame.height * scale))
    
        try:
            resized = frame.convert('RGBA').resize((w, h), Image.NEAREST)
            alpha = resized.split()[3]
            alpha = alpha.point((lambda a: if a >= 128:
    255))
            resized.putalpha(alpha)
            bg = None('RGB', (w, h), (255, 0, 255))
            bg.paste(resized, (0, 0), resized)
            self._tkimg = None(bg)
            self.label.configure(image = self._tkimg)
            self._img_w, self._img_h = w, h
            if self._dragging:
            
                try:
                    self.win.geometry(f'''{w}x{h}''')
                    return None
                
                    try:
                        self.win.geometry(f'''{w}x{h}+{left}+{top}''')
                        if not self._first_positioned:
                        
                            try:
                                self.win.deiconify()
                                self._first_positioned = True
                                return None
                                return None
                                except Exception:
                                    Image.new
                                    return None
                                except Exception:
                                    Image.new
                                    return None
                            except Exception:
                                Image.new
                                return None






    def _layout_offset(self):
        '''진열 방식(일자/3+2 세로 그룹)에 따라 본체 기준 (거리, 좌우엇갈림, 상하오프셋)을
    계산한다. 거리는 항상 양수로 반환하고, 실제 좌우 반전은 호출부(step)에서 방향에
    맞춰 처리한다. group32는 앞 3마리를 세로로 한 줄, 뒤 2마리를 세로로 한 줄 쌓는다
    (옆으로 나란히가 아니라 위아래로 쌓아서 진짜 "세로 대열"처럼 보이게).
    (버그 수정) 예전엔 이 간격들이 전부 고정 픽셀값이라, 설정의 "펫 크기" 슬라이더로
    본체/동료 스프라이트를 크게 키우면 스프라이트만 커지고 간격은 그대로라 서로
    겹쳐 보이는 문제가 있었다. 이제 manual_scale(펫 크기 배율)을 그대로 곱해서
    커질수록 간격도 같이 넓어지게 했다.'''
        scale = self.owner.state.get('manual_scale', 1)
        if self.is_body2:
            return (30 * scale, 0, 38 * scale)
        layout = None.owner.state.get('companion_layout', 'line')
        i = self.slot_index
        if layout == 'group32':
            col = i // 3
            within = i % 3
            dist = (80 + col * 66) * scale
            dy = -44 * within * scale
            return (dist, 0, dy)
        return ((None + i * 58) * scale, 0, 0)


    def set_synced_sleep(self, sleeping):
        self._synced_sleep = bool(sleeping)


    def _step_free_roam(self, dt_ms):
        """자유롭게 배회 모드: 키보드 조작과 무관하게 각자 알아서 화면(바탕화면 범위) 안을
    상하좌우로 걸어다니다가, 서로 너무 가까워지면(_check_companion_collisions에서
    감지) 잠깐 넘어지는 연출을 보여준다. 방향이 정반대로 바뀔 땐 잠깐 '몸을 돌리는'
    연출(있으면 react 동작, 없으면 그냥 걷기)을 넣어서 갑자기 홱 뒤집히지 않게 한다."""
        now = None()
        if self.free_x is None:
            sw = max(1, self.owner.screen_w)
            spread_x = self.owner.screen_left + (self.slot_index * 137 + 60) % sw
            self.free_x = spread_x
            self.free_y = self.owner._get_floor_y()
            self.free_target_y = self.free_y
            self.direction = self.owner.direction
            self.free_state = 'idle'
            self._free_target_x = self.free_x
            self._free_next_decision_at = random.uniform + None(0, 1)
            self._turn_until = 0
        min_x = self.owner.screen_left + 30
        max_x = self.owner.screen_left + self.owner.screen_w - 30
        if max_x <= min_x:
            max_x = min_x + 1
        min_y = self.owner.screen_top + 30
        max_y = self.owner.screen_top + self.owner.screen_h - 30
        if max_y <= min_y:
            max_y = min_y + 1
        if not isinstance(self.free_x, (int, float)):
            self.free_x = min_x
        if not isinstance(self.free_y, (int, float)):
            self.free_y = min_y
        self.free_x = max(min_x, min(max_x, self.free_x))
        self.free_y = max(min_y, min(max_y, self.free_y))
        if self.free_state == 'fallen':
            if not self.entry.get('react'):
                self.entry.get('react')
                if not self.entry.get('land'):
                    self.entry.get('land')
            fall_action = self.entry['idle']
            if self.anim_set.has(fall_action):
                self.action = fall_action
            if now >= self._free_fallen_until:
                self.free_state = 'idle'
                self.action = self.entry['idle']
                self.frame_idx = 0
                self._free_next_decision_at = random.uniform + None(1, 2.5)
            return None
        if (now + 0.3 + (self.slot_index % 5) * 0.5).free_state == 'playing':
            if not self.entry.get('trick'):
                self.entry.get('trick')
                if not self.entry.get('react'):
                    self.entry.get('react')
            play_action = self.entry['idle']
            if self.anim_set.has(play_action):
                self.action = play_action
            if now >= self._free_playing_until:
                self.free_state = 'idle'
                self.action = self.entry['idle']
                self.frame_idx = 0
                self._free_next_decision_at = random.uniform + None(1, 2.5)
            return None
        if None >= time.time._free_next_decision_at:
            pass
        if self.free_state == 'walk':
            speed = 40 * (dt_ms / 1000)
            dx = self._free_target_x - self.free_x
            dy = self.free_target_y - self.free_y
            dist = None(dx, dy)
            if dist > 2:
                step_len = min(speed, dist)
                self.free_x = max(min_x, min(max_x, self.free_x + (dx / dist) * step_len))
                self.free_y = max(min_y, min(max_y, self.free_y + (dy / dist) * step_len))
                new_dir = _dir_from_vector(dx, dy)
            if now < self._turn_until:
                turn_action = self.entry.get('react')
                if turn_action and self.anim_set.has(turn_action):
                    pass
                elif self.anim_set.has('Walk'):
                    pass
            
                self.action = self.entry['idle']
                return None
            self.action = 'Walk' if now if None() < 0.7 else now if new_dir is not None else math.hypot.anim_set.has('Walk') else self.entry['idle']
            return None
        self.action = now if None() < 0.7 else now.entry['idle']


    def play_trick(self):
        '''trick'''
        if self.entry:
            if not self.entry.get('trick'):
                self.entry.get('trick')
            self.action = self.entry['idle']
            self.frame_idx = 0
            return None


    def back_to_idle(self):
        '''idle'''
        if self.entry:
            self.action = self.entry['idle']
            return None


    def destroy(self):
    
        try:
            self.win.destroy()
            return None
        except Exception:
            return None


    __static_attributes__ = ('_dragging', '_elapsed', '_first_positioned', '_free_fallen_until', '_free_next_decision_at', '_free_playing_until', '_free_target_x', '_img_h', '_img_w', '_press_widget_x', '_press_widget_y', '_press_x_root', '_press_y_root', '_synced_sleep', '_tkimg', '_turn_until', 'action', 'anim_set', 'dex', 'direction', 'entry', 'frame_idx', 'free_state', 'free_target_y', 'free_x', 'free_y', 'is_body2', 'label', 'level', 'mega', 'owner', 'slot_index', 'win')
    __classdictcell__ = __classdict__
