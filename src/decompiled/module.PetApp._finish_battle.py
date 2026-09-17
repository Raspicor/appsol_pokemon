# module.PetApp._finish_battle
# source line 11305
# Recovered from bytecode; default argument values are not shown.

def _finish_battle(self, ctx, caught, entered_fight):
    ui = ctx['update_ui']
    if ui.get('set_locked'):
        None(True)
    self.root.after(1300, (lambda : self._close_battle(ctx, caught = caught, entered_fight = entered_fight)))
