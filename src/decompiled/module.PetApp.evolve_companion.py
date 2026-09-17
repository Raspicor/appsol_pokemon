# module.PetApp.evolve_companion
# source line 7626
# Recovered from bytecode; default argument values are not shown.

def evolve_companion(self, d, forced_branch):
    status = self.companion_evolution_status(d)
    if not status.get('evolvable') or status.get('ready'):
        return False
    d = None(d)
    if status.get('is_eevee'):
        branches = SPECIES['eevee'].get('branches', { })
        branch = forced_branch if forced_branch and forced_branch in branches else self._predict_eevee_branch()
        next_dex = branches[branch]['dex']
        next_entry = POKEDEX.get(next_dex)
        if not next_entry:
            return False
    next_dex = status['next_dex']
    next_entry = status['next_entry']
    entry = POKEDEX.get(d, { })
    caught = self.state.setdefault('caught', { })
    dex_rec = self.state.setdefault('dex', { })
    party = self.state.get('party', [])

    try:
        i = party.index(d)
        old_rec = caught.get(str(d), { })
        old_level = old_rec.get('level', 1)
        prev_next_level = caught.get(str(next_dex), { }).get('level', 0)
        next_remaining = max(0, next_entry.get('chain_len', 1) - 1 - next_entry.get('stage', 0))
        next_max_level = max_level_for_remaining(next_remaining)
        boosted_level = min(next_max_level, max(old_level, prev_next_level) + 1)
        if not old_rec.get('lineage'):
            old_rec.get('lineage')
        prev_lineage = [
            d]
        new_lineage = prev_lineage + [
            next_dex]
        caught[str(next_dex)] = {
            'lineage': new_lineage,
            'raised': True,
            'level': boosted_level }
        dex_rec[str(next_dex)] = 'caught'
        new_party = list(party)
        new_party[i] = next_dex
        self.state['party'] = new_party
        started_map = self.state.setdefault('companion_evolve_started', { })
        started_map.pop(str(d), None)
        started_map[str(next_dex)] = None()
        hidden_list = self.state.get('party_hidden', [])
        if d in hidden_list or str(d) in hidden_list:
            for None in :
                pass
            x, self.state['party_hidden'] = , [], 
        notified = self.state.get('evolve_ready_notified', [])
        for None in :
            if not k != f'''companion:{d}''':
                continue
        k, self.state['evolve_ready_notified'] = , [], 
        self._rebuild_companions()
        self.save_state()
    
        try:
            if self.tray_icon:
            
                try:
                    self.tray_icon.notify(f'''동료 {entry.get('kr', '?')}이(가) {next_entry.get('kr', '?')}(으)로 진화했어요!''', 'PikaPet')
                    return True
                    except ValueError:
                        hidden_list, x
                        i = party.index(str(d))
                        continue
                        except ValueError:
                            return False
                
                
                except Exception:
                    hidden_list, x
                    return True
