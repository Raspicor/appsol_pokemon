# module.PetApp.start_free_walk
# source line 9252
# Recovered from bytecode; default argument values are not shown.

def start_free_walk(self):
    span = 160
    target_x = random.randint + None(-span, span)
    target_x = max(self.screen_left + 40, min(self.screen_left + self.screen_w - 40, target_x))
    target_y = None
    if self.state.get('body_free_direction') and self.ground_mode == 'floor':
        min_y = self.screen_top + 60
        max_y = self._get_floor_y()
        target_y = random.randint + None(-140, 140)
        target_y = max(min_y, min(max_y, target_y))
    self.start_targeted_walk(target_x, self._finish_to_idle, target_y = target_y)
