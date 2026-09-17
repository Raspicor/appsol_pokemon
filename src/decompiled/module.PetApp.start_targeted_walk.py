# module.PetApp.start_targeted_walk
# source line 9266
# Recovered from bytecode; default argument values are not shown.

def start_targeted_walk(self, target_x, on_arrive, target_y):
    self.behavior_state = 'walk'
    self._walk_target_x = target_x
    self._walk_target_y = target_y if target_y is not None else self.pos_y
    self._walk_on_arrive = on_arrive
    if target_y is not None:
        nd = _dir_from_vector(target_x - self.pos_x, self._walk_target_y - self.pos_y)
        self.direction = nd if nd is not None else self.direction
    elif target_x > self.pos_x:
        pass

    self.direction = spriteanim.DIR_LEFT
    self.walk_facing_dir = self.direction
    self.play_action('Walk', loop = True)
