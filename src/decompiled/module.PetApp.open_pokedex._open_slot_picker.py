# module.PetApp.open_pokedex._open_slot_picker
# source line 16280
# Recovered from bytecode; default argument values are not shown.

def _open_slot_picker(d):
    cap = companion_slot_count(self.state)
    party = list(self.state.get('party', []))
    pick_win = None(win)
    pick_win.title('어느 칸에 넣을까요?')
    resolve_species_win(pick_win, 280, 100)
    None(pick_win, text = f'''{POKEDEX.get(d, { }).get('kr', '?')}을(를) 어느 칸에 넣을까요?''', font = ('맑은 고딕', 9), wraplength = 250, justify = 'left').pack(padx = 10, pady = (10, 6))

    def _do_insert(pos):
        '''party'''
        new_party = list(self.state.get('party', []))
        new_party.insert(pos, d)
        self.state['party'] = new_party[:cap]
        self._rebuild_companions()
        self.save_state()
        pick_win.destroy()
        None()

    for pos in range(len(party) + 1):
        slot_no = pos + 2
        None(pick_win, text = label, command = (lambda p = pos: None(p))).pack(fill = 'x', padx = 10, pady = 2)
    tk.Label if pos < len(party) else range(len(party) + 1)
    None(pick_win, text = '취소', command = pick_win.destroy).pack(pady = (4, 10))
