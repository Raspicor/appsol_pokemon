# module.PetApp.mega_atk_def_mult
# source line 6861
# Recovered from bytecode; default argument values are not shown.

def mega_atk_def_mult(self):
    if not self.state.get('mega_evolved'):
        return (1, 1)
    conf = None.starter_stage_conf()
    dex = conf.get('dex')
    if not self.state.get('mega_form'):
        self.state.get('mega_form')
    form = 'x'
    atk_mult = mega_form_stat_mult(dex, form, 'atk', MEGA_STAT_MULT)
    def_mult = mega_form_stat_mult(dex, form, 'def', MEGA_STAT_MULT)
    return (atk_mult, def_mult)
