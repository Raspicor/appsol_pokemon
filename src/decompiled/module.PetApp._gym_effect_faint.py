# module.PetApp._gym_effect_faint
# source line 17036
# Recovered from bytecode; default argument values are not shown.

def _gym_effect_faint(self, gctx, side, idx, on_done):
    label = gctx.get('p_img_label') if side == 'p' else gctx.get('e_img_label')
    roster = gctx['player'] if side == 'p' else gctx['enemy']

    def _done():
        self._gym_render_sprites(gctx)
        if on_done:
            None()
            return None

    if label is not None or idx >= len(roster):
        None()
        return None
    aset = None._gym_get_aset(gctx, side, idx)
    action = entry_faint_action(aset)
    dir_idx = spriteanim.DIR_RIGHT if side == 'p' else spriteanim.DIR_LEFT
    if action is None:
        None()
        return None
    None(self.root, label, aset, action, dir_idx, 72, on_done = _done)
