# module.PetApp._gym_render_sprites
# source line 16976
# Recovered from bytecode; default argument values are not shown.

def _gym_render_sprites(self, gctx):
    TARGET_H = 72
    ei = gctx['e_active']
    pi = gctx['p_active']

    def _sprite_scale_for(m):
        '''종/메가진화 여부에 따라 전투 스프라이트 크기를 다르게 준다 - 메가진화는
    조금 더 크게, 루기아/펄기아/아르세우스는 메가진화보다도 더 크게.'''
    
        try:
            dex = int(m.get('entry', { }).get('dex'))
            if dex in BATTLE_SPRITE_BIG_LEGEND_DEX:
                return BATTLE_SPRITE_BIG_LEGEND_SCALE
            fix = None.get(dex, 1)
            if m.get('mega'):
                return BATTLE_SPRITE_MEGA_SCALE * fix
            return None
        except Exception:
            dex = None
            continue



    def _draw(label, roster, hp_list, idx, side, dir_idx):
        if label is None:
            return None
        if None >= len(roster):
            return None
        m = None[None]
        aset = self._gym_get_aset(gctx, side, idx)
        idle_act = 'Idle' if side == 'p' and m.get('kind') == 'body' else m['entry'].get('idle', 'Idle')
        frame = aset.frame(idle_act, 0, dir_idx) if aset else None
        tkimg = None(img)
        label.image = tkimg
        label.configure(image = tkimg)

    None(gctx.get('p_img_label'), gctx['player'], gctx['p_hp'], pi, 'p', spriteanim.DIR_RIGHT)
    None(gctx.get('e_img_label'), gctx['enemy'], gctx['e_hp'], ei, 'e', spriteanim.DIR_LEFT)
