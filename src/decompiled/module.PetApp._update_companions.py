# module.PetApp._update_companions
# source line 7436
# Recovered from bytecode; default argument values are not shown.

def _update_companions(self, dt, now):
    if self.body2 is not None:
    
        try:
            self.body2.step(dt * 1000)
            if not self.companions:
                return None
            layout = None.state.get('companion_layout', 'line')
            if layout in ('line', 'group32'):
                layout in ('line', 'group32')
            sync_sleep = self.behavior_state == 'sleep'
            for c in self.companions:
                c.set_synced_sleep(sync_sleep)
                c.step(dt * 1000)
            if layout == 'free':
                self._check_companion_collisions(now)
                return None
            if None.behavior_state == 'idle':
                if random.uniform > None(45, 90):
                    self._last_duo_trick = now
                    if not self.resolve('trick'):
                        self.resolve('trick')
                    trick_name = 'Idle'
                    self.play_action(trick_name, loop = False, on_complete = self._finish_to_idle)
                    for c in self.companions:
                        c.play_trick()
                    now - self._last_duo_trick
                    self.root.after(1500, (lambda : for None in :
    c = Nonec,))
                    return None
                return now - self._last_duo_trick
            return None
        except Exception:
            continue
