# module.PetApp.open_preset_editor._render_slots
# source line 15428
# Recovered from bytecode; default argument values are not shown.

def _render_slots():
    for w in slot_inner.winfo_children():
        w.destroy()
    slot_photo_cache.clear()
    cat = state_box['category']
    slots = self._get_preset_slots(cat)
    caught = self.state.get('caught', { })
    for None in enumerate(slots):
        i = ()
        dex = None
        None(cell, text = f'''{i + 1}번''', font = ('맑은 고딕', 8), width = 4, anchor = 'w').pack(side = 'left')
        cell.bind('<Button-1>', (lambda e, idx = i: None(idx)))
        for child in cell.winfo_children():
            child.bind('<Button-1>', (lambda e, idx = i: None(idx)))
        tk.Button if dex else tk.Label
    tk.Label
    None()
