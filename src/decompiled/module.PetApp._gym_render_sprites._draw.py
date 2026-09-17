# module.PetApp._gym_render_sprites._draw
# source line 16995
# Recovered from bytecode; default argument values are not shown.

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
