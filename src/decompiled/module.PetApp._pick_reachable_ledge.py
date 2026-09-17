# module.PetApp._pick_reachable_ledge
# source line 11589
# Recovered from bytecode; default argument values are not shown.

def _pick_reachable_ledge(self, ledges):
    candidates = []
    for lg in ledges:
        if lg['top'] < 0 or lg['top'] >= self.pos_y - 20:
            continue
        visible_left = max(self.screen_left, lg['left'])
        visible_right = min(self.screen_left + self.screen_w, lg['right'])
        if visible_right - visible_left <= 60:
            continue
        clamped = dict(lg)
        clamped['left'] = visible_left
        clamped['right'] = visible_right
        candidates.append(clamped)
    if not candidates:
        return None
    None.sort(key = (lambda lg: abs((lg['left'] + lg['right']) / 2 - self.pos_x)))
    return candidates[0]
