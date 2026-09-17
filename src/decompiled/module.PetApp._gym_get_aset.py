# module.PetApp._gym_get_aset
# source line 16950
# Recovered from bytecode; default argument values are not shown.

def _gym_get_aset(self, gctx, side, idx):
    cache = gctx.setdefault('aset_cache', { })
    key = (side, idx)
    if key in cache:
        return cache[key]
    aset = None

    try:
        roster = gctx['player'] if side == 'p' else gctx['enemy']
        if idx < len(roster):
            m = roster[idx]
            sprite_name = m['entry'].get('en')
            if side == 'p' and m.get('kind') == 'body':
                aset = self.active_anim_set()
            else:
            
                try:
                    if m.get('mega'):
                    
                        try:
                            mega_folder = companion_mega_sprite_folder(m['entry'])
                            if mega_folder:
                                sprite_name = mega_folder
                            if sprite_name:
                            
                                try:
                                    aset = None(sprite_folder_path(sprite_name))
                                    cache[key] = aset
                                    return aset
                                except Exception:
                                    aset = None
                                    continue
