# module.PetApp.evolve
# source line 8146
# Recovered from bytecode; default argument values are not shown.

def evolve(self, forced_branch):
    sp = SPECIES[self.state['starter']]
    self.state['stage'] = self.state.get('stage', 0) + 1
    if sp.get('branching') and self.state['stage'] >= 1:
        if forced_branch and forced_branch in sp.get('branches', { }):
            best = forced_branch
        else:
            best = self._predict_eevee_branch()
        self.state['eevee_branch'] = best
    self.state['stage_started_at'] = None()
    self.state['quota_days_done'] = 0
    self.state['catch_counts'] = {
        '5': 0,
        '4': 0,
        '3': 0,
        '2': 0,
        '1': 0 }
    notified = self.state.get('evolve_ready_notified', [])
    for None in :
        k = None
        if not k != 'body':
            continue

    k, self.state['evolve_ready_notified'] = notified, k, , []
    self.save_state()

    try:
        self.trigger_fx('evolve')
        if not self.resolve('trick'):
            self.resolve('trick')
        trick_name = 'Idle'
        self.behavior_state = 'acting'
        self.play_action(trick_name, loop = False, on_complete = self._finish_to_idle)
    
        try:
            if self.tray_icon:
            
                try:
                    self.tray_icon.icon = self._tray_image()
                    return None
                    return None
                
                    except Exception:
                        None, None, time.time
                        continue
                except Exception:
                    return None
