# module.PetApp.mega_display_name_for
# source line 6917
# Recovered from bytecode; default argument values are not shown.

def mega_display_name_for(self, form):
    conf = self.starter_stage_conf()
    names = MEGA_NAME_KR.get(conf.get('dex'))
    if isinstance(names, dict):
        if not form:
            form
            if not self.state.get('mega_form'):
                self.state.get('mega_form')
        return names.get('x')
