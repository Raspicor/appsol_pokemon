# module.PetApp._companion_level_short_text
# source line 7891
# Recovered from bytecode; default argument values are not shown.

def _companion_level_short_text(self, d):
    try:
        d = int(d)
        cur_level = self.state.get('caught', { }).get(str(d), { }).get('level', 1)
        remain = self.companion_level_remaining_n(d)
        if remain is None:
            return f'''Lv.{cur_level}(최고)'''
        if None == 0:
            return f'''Lv.{cur_level}(✅레벨업 가능)'''
        return f'''{cur_level}({remain}마리 남음)'''
    except Exception:
        return ''
