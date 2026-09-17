# module.Companion.play_trick
# source line 4451
# Recovered from bytecode; default argument values are not shown.

def play_trick(self):
    if self.entry:
        if not self.entry.get('trick'):
            self.entry.get('trick')
        self.action = self.entry['idle']
        self.frame_idx = 0
        return None
