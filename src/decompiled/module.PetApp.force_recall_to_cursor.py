# module.PetApp.force_recall_to_cursor
# source line 11512
# Recovered from bytecode; default argument values are not shown.

def force_recall_to_cursor(self):
    try:
        x = self.root.winfo_pointerx()
        y = self.root.winfo_pointery()
        self.force_recall_to(x, y)
        return None
    except Exception:
        y = self._get_floor_y()
        x = self.screen_left + self.screen_w // 2
        continue
