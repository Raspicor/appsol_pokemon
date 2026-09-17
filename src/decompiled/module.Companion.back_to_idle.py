# module.Companion.back_to_idle
# source line 4456
# Recovered from bytecode; default argument values are not shown.

def back_to_idle(self):
    if self.entry:
        self.action = self.entry['idle']
        return None
