# module.PetApp.force_recall_primary_center
# source line 11501
# Recovered from bytecode; default argument values are not shown.

def force_recall_primary_center(self):
    try:
        pw = self.root.winfo_screenwidth()
        ph = self.root.winfo_screenheight()
        self.force_recall_to(pw // 2, ph // 2)
        return None
    except Exception:
        ph = 600
        pw = 800
        continue
