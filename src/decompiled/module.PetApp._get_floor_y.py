# module.PetApp._get_floor_y
# source line 4915
# Recovered from bytecode; default argument values are not shown.

def _get_floor_y(self):
    fallback = self.screen_top + self.screen_h - GROUND_MARGIN
    if self.taskbar_rect:
        floor_y = self.taskbar_rect[1]
        if floor_y < self.screen_top + self.screen_h * 0.5:
            return fallback
        if None > None.screen_top + self.screen_h + 200:
            return fallback
        return None
