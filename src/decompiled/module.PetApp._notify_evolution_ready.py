# module.PetApp._notify_evolution_ready
# source line 7542
# Recovered from bytecode; default argument values are not shown.

def _notify_evolution_ready(self, key, msg):
    notified = self.state.setdefault('evolve_ready_notified', [])
    if key in notified:
        return None
    None.append(key)
    self.save_state()

    try:
        if self.tray_icon:
        
            try:
                self.tray_icon.notify(msg, 'PikaPet')
                return None
            
                try:
                    None('진화 가능!', msg)
                    return None
                except Exception:
                    return None
