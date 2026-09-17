# module.PetApp._refresh_icons_if_needed
# source line 11579
# Recovered from bytecode; default argument values are not shown.

def _refresh_icons_if_needed(self):
    now = None()
    if now - self._icons_cache_at > 15:
    
        try:
            self._icons_cache = None()
            self._icons_cache_at = now
            return self._icons_cache
        except Exception:
            self._icons_cache = []
            continue
