# module.PetApp._mine_marker_frames
# source line 11935
# Recovered from bytecode; default argument values are not shown.

def _mine_marker_frames(self, target_h):
    try:
        entry = self.player_pokedex_entry()
        aset = None(sprite_folder_path(entry.get('en', '')))
        if aset.has('Walk'):
            pass
        elif not entry.get('idle'):
        
            try:
                entry.get('idle')
                anim_name = 'Idle'
                n = max(1, aset.n_frames(anim_name))
                right_imgs = []
                durations = []
                for i in range(n):
                    f = aset.frame(anim_name, i, spriteanim.DIR_RIGHT)
                    if f is None:
                        f = aset.frame(anim_name, i, spriteanim.DIR_DOWN)
                    if f is None:
                        raise ValueError('스프라이트 프레임을 찾을 수 없음')
                    f = f.convert('RGBA')
                    scale = target_h / max(1, f.height)
                    f = f.resize((max(8, int(f.width * scale)), target_h), Image.NEAREST)
                    right_imgs.append(f)
                    durations.append(max(40, aset.duration_of(anim_name, i) * ANIM_TICK_MS))
                'Walk'
                for None in :
                    pass
                ImageTk.PhotoImage
            
                try:
                    None = 
                    im = , []
                    for None in :
                        pass
                    ImageTk.PhotoImage
                
                    try:
                        None = 
                        im = , []
                        return (right_photos, left_photos, durations)
                    
                        try:
                        
                        
                        except Exception:
                            right_imgs, im
                            draw_pokeball_image(target_h) = spriteanim.AnimSet
                            photo = None(img)
                            return 
