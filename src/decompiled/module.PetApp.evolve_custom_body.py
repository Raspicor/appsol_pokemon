# module.PetApp.evolve_custom_body
# source line 7695
# Recovered from bytecode; default argument values are not shown.

def evolve_custom_body(self):
    custom_dex = self.state.get('custom_body_dex')
    if not custom_dex:
        return False
    d = None(custom_dex)
    status = self.companion_evolution_status(d)
    if not status.get('evolvable') or status.get('ready'):
        return False
    next_dex = None['next_dex']
    next_entry = status['next_entry']
    entry = POKEDEX.get(d, { })
    caught = self.state.setdefault('caught', { })
    dex_rec = self.state.setdefault('dex', { })
    old_rec = caught.get(str(d), { })
    if str(next_dex) not in caught:
        caught[str(next_dex)] = {
            'level': old_rec.get('level', 1) }
    if not old_rec.get('lineage'):
        old_rec.get('lineage')
    prev_lineage = [
        d]
    caught[str(next_dex)]['raised'] = True
    caught[str(next_dex)]['lineage'] = prev_lineage + [
        next_dex]
    dex_rec[str(next_dex)] = 'caught'
    self.state['custom_body_dex'] = next_dex
    started_map = self.state.setdefault('companion_evolve_started', { })
    started_map.pop(str(d), None)
    started_map[str(next_dex)] = None()
    notified = self.state.get('evolve_ready_notified', [])
    for None in :
        k = None
        if not k != f'''body_swap:{d}''':
            continue

    k, self.state['evolve_ready_notified'] = notified, k, , []
    self._ensure_body_anim_loaded(next_dex)
    self.save_state()

    try:
        self._finish_to_idle()
        self.redraw()
    
        try:
            if self.tray_icon:
            
                try:
                    self.tray_icon.notify(f'''본체 {entry.get('kr', '?')}이(가) {next_entry.get('kr', '?')}(으)로 진화했어요!''', 'PikaPet')
                    return True
                
                    except Exception:
                        None, None, time.time
                        continue
                except Exception:
                    return True
