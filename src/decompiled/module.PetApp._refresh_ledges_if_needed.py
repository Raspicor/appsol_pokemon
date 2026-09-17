# module.PetApp._refresh_ledges_if_needed
# source line 11569
# Recovered from bytecode; default argument values are not shown.

def _refresh_ledges_if_needed(self, force):
    now = None()
    if force or now - self._ledges_cache_at > 5:
    
        try:
            self._ledges_cache = None(exclude_titles = [
                'PikaPet'])
            self._ledges_cache_at = now
            return self._ledges_cache
        except Exception:
            self._ledges_cache = []
            continue
