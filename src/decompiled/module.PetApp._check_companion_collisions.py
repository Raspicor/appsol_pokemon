# module.PetApp._check_companion_collisions
# source line 7459
# Recovered from bytecode; default argument values are not shown.

def _check_companion_collisions(self, now):
    busy_states = ('fallen', 'playing')
    pool = list(self.companions)
    if self.body2 is not None:
        pool.append(self.body2)
    for None in roaming,:
        if getattr(c, 'free_x', None) is None:
            continue
        if not c.free_state not in busy_states:
            continue
        if getattr(c, '_dragging', False):
            continue
    roaming, = , []
    c = pool, c
    affection = float(self.state.get('affection', 50))
    play_chance = max(0, min(0.7, (affection / 100) * 0.7))
    for i in range(len(roaming)):
        a = roaming[i]
        for j in range(i + 1, len(roaming)):
            b = roaming[j]
            if b.free_state in busy_states or getattr(b, '_dragging', False):
                continue
            if not None(a.free_x - b.free_x, a.free_y - b.free_y) < 34:
                continue
            b, b.free_x += 20, .free_x
        random.uniform if None() < play_chance else random.uniform
    math.hypot
    return None
