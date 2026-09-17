# module.PetApp._apply_body1_visibility
# source line 7128
# Recovered from bytecode; default argument values are not shown.

def _apply_body1_visibility(self):
    if self.body_visibility('p1'):
        self.body_visibility('p1')
    should_show = not self.state.get('in_ball', False)

    try:
        if should_show:
        
            try:
                self.root.deiconify()
            try:
                self.root.withdraw()
                self._apply_companion_ball_visibility()
                return None
            except Exception:
                continue
