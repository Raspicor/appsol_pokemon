# module.PetApp._legend_bundle_for_dex
# source line 13502
# Recovered from bytecode; default argument values are not shown.

def _legend_bundle_for_dex(self, gen, dex):
    for b in self._legend_bundles(gen):
        if not int(b.get('dex', -1)) == int(dex):
            continue
    
        return self._legend_bundles(gen), b
