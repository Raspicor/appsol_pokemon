# module.PetApp.tick
# source line 7337
# Recovered from bytecode; default argument values are not shown.

def tick(self):
    now = None()

    try:
        dt = now - self._last_tick if self._last_tick else TICK_MS / 1000
        dt = max(0, min(dt, 0.5))
        self._last_tick = now
        self.state['active_seconds'] = self.state.get('active_seconds', 0) + dt
        self._decay_hunger(dt)
        self.check_evolution()
        if now - self._last_companion_evo_check > 20:
            self._last_companion_evo_check = now
            self.check_companion_evolution()
            self.check_companion_leveling()
        if now - self._last_screen_check > 4:
            self._last_screen_check = now
            self._refresh_screen_bounds()
        if now - self._last_topmost_reassert > 10:
            self._last_topmost_reassert = now
            self._reassert_topmost()
        if self.state.get('in_ball'):
        
            try:
                self._periodic_save(now)
                self.root.after(TICK_MS, self.tick)
                return None
            
                try:
                    if not self.battle_open:
                    
                        try:
                            if self.behavior_state != 'held':
                                self.advance_animation(dt * 1000)
                            self.update_behavior(dt, now)
                            self.redraw()
                            self._update_companions(dt, now)
                        
                            try:
                                self._periodic_save(now)
                                self.root.after(TICK_MS, self.tick)
                                return None
                                except Exception:
                                    continue
                                except Exception:
                                    _tick_exc = None
                                    self._log_tick_error(_tick_exc)
                                
                                    try:
                                        _tick_exc = None
                                        del _tick_exc
                                        continue
                                        except Exception:
                                        
                                            try:
                                                _tick_exc = None
                                                del _tick_exc
                                                continue
                                                _tick_exc = None
                                                del _tick_exc
                                            
                                                try:
                                                    except Exception:
                                                        continue
                                                except:
                                                    self._periodic_save(now)
                                                except Exception:
                                                    pass

                                                self.root.after(TICK_MS, self.tick)
