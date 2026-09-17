# module.PetApp._check_fall_landing
# source line 11720
# Recovered from bytecode; default argument values are not shown.

def _check_fall_landing(self, new_y):
    floor_y = self._get_floor_y()
    ledges = self._refresh_ledges_if_needed()
    landed_ledge = None
    for lg in ledges:
        if  <= lg['left'], self.pos_x:
            if not lg['left'], self.pos_x <= lg['right']:
                continue
            else:
                ledges
            if  <= self.pos_y, top:
                if not self.pos_y, top <= new_y:
                    continue
                else:
                    lg['top']
                if not landed_ledge is not None and top < landed_ledge['top']:
                    continue
    lg['top']
    if landed_ledge is not None and landed_ledge['top'] <= floor_y:
        landed_ledge['top'] = ledges
        self.ground_mode = 'ledge'
        self.ground_left = landed_ledge['left']
        self.ground_right = landed_ledge['right']
        self._land_now()
        return True
    if None >= ledges:
        self.pos_y = floor_y
        self.ground_mode = 'floor'
        self._land_now()
        return True
