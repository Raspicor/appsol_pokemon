# module.Companion._layout_offset
# source line 4311
# Recovered from bytecode; default argument values are not shown.

def _layout_offset(self):
    scale = self.owner.state.get('manual_scale', 1)
    if self.is_body2:
        return (30 * scale, 0, 38 * scale)
    layout = None.owner.state.get('companion_layout', 'line')
    i = self.slot_index
    if layout == 'group32':
        col = i // 3
        within = i % 3
        dist = (80 + col * 66) * scale
        dy = -44 * within * scale
        return (dist, 0, dy)
    return ((None + i * 58) * scale, 0, 0)
