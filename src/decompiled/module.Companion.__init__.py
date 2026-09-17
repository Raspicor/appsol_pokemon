# module.Companion.__init__
# source line 4100
# Recovered from bytecode; default argument values are not shown.

def __init__(self, owner, dex, level, slot_index, mega, is_body2):
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
