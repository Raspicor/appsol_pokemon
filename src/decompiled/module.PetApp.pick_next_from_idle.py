# module.PetApp.pick_next_from_idle
# source line 9210
# Recovered from bytecode; default argument values are not shown.

def pick_next_from_idle(self):
    now = None()
    hunger = self.state.get('hunger', 80)
    if hunger < HUNGRY_REACT_THRESHOLD and None() < 0.35:
        self._do_one_shot('hungry', bonus_quota = False)
        return None
    affection = random.random.state.get('affection', 50)
    if affection >= AFFECTION_HAPPY_THRESHOLD and None() < 0.3:
        self._do_one_shot('happy', bonus_quota = False)
        return None
    if time.time - random.random.state.get('last_interact_time', 0) > 300 and None() < 0.25:
        self.enter_sleep()
        return None
    ledges = random.random._refresh_ledges_if_needed()
    icons = self._refresh_icons_if_needed()
    roll = None()
    if roll < 0.45:
        self.start_free_walk()
        return None
    if random.random < 0.6:
        if self.state.get('pet_hide_seconds', 8) > 0:
            self.begin_hide_sequence()
            return None
        target = self._pick_reachable_ledge(ledges) if None else None
        if target:
            self.begin_jump_to_ledge(target)
            return None
        None.start_free_walk()
        return None
    if None < 0.8 and ledges:
        target = self._pick_reachable_ledge(ledges)
        if target:
            self.begin_jump_to_ledge(target)
            return None
        None.start_free_walk()
        return None
    if None < 0.93 and icons:
        random.choice(None(icons))
        return None
    None.enter_idle()
