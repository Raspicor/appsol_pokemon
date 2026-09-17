# module.PetApp.mega_sprite_folder_candidates
# source line 6882
# Recovered from bytecode; default argument values are not shown.

def mega_sprite_folder_candidates(self):
    conf = self.starter_stage_conf()
    if not conf.get('id'):
        conf.get('id')
    sid = ''
    names = MEGA_NAME_KR.get(conf.get('dex'))
    if isinstance(names, dict):
        return [
            ('x', f'''{sid}-mega-x'''),
            ('x', f'''{sid}_mega_x'''),
            ('y', f'''{sid}-mega-y'''),
            ('y', f'''{sid}_mega_y''')]
    if None:
        return [
            (None, f'''{sid}-mega'''),
            (None, f'''{sid}_mega''')]
