# module.PetApp._gym_effect
# source line 17020
# Recovered from bytecode; default argument values are not shown.

def _gym_effect(self, gctx, side, idx, crit):
    label = gctx.get('p_img_label') if side == 'p' else gctx.get('e_img_label')
    roster = gctx['player'] if side == 'p' else gctx['enemy']
    if label is not None or idx >= len(roster):
        return None
    m = None[None]
    aset = self._gym_get_aset(gctx, side, idx)
    action = entry_attack_action(m['entry'], aset)
    dir_idx = spriteanim.DIR_RIGHT if side == 'p' else spriteanim.DIR_LEFT
    play_sprite_action(self.root, label, aset, action, dir_idx, 72, on_done = (lambda : self._gym_render_sprites(gctx)))
