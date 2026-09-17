# module.PetApp.mega_has_dual_form
# source line 6875
# Recovered from bytecode; default argument values are not shown.

def mega_has_dual_form(self):
    conf = self.starter_stage_conf()
    return isinstance(MEGA_NAME_KR.get(conf.get('dex')), dict)
