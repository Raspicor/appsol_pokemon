# module.PetApp.open_evolution_tab._render_eevee_chain
# source line 8473
# Recovered from bytecode; default argument values are not shown.

def _render_eevee_chain(parent, sel_d):
    if not bool(dex_state.get('133')):
        bool(dex_state.get('133'))
    base_colored = own_species == 'eevee'
    cell = None(parent, 133, base_colored, 48, sel_d == 133)
    cell.pack(side = 'left', padx = 4)
    None(cell, text = '이브이' if base_colored else '？？？', font = ('맑은 고딕', 7)).pack()
    None(parent, text = '→', font = ('맑은 고딕', 12)).pack(side = 'left')
    branch_wrap = None(parent)
    branch_wrap.pack(side = 'left')
    branch_cols = 3
    for None(branch_wrap, bd, colored, 36, sel_d == bd) in enumerate(EEVEE_BRANCH_BY_DEX.items()):
        bd = ()
        bkey = (idx,)
        if not bool(dex_state.get(str(bd))):
            bool(dex_state.get(str(bd)))
            if own_species == 'eevee':
                own_species == 'eevee'
                if own_stage_idx >= 1:
                    own_stage_idx >= 1
        r = ()
        c = divmod(idx, branch_cols)
        bcell.grid(row = r, column = c, padx = 2, pady = 1)
        None(bcell, text = bname, font = ('맑은 고딕', 7)).pack()
    POKEDEX.get(bd, { }).get('kr', '?') if colored else '？？？'
