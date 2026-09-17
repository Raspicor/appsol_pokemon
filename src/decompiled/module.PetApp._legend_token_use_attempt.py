# module.PetApp._legend_token_use_attempt
# source line 13509
# Recovered from bytecode; default argument values are not shown.

def _legend_token_use_attempt(self, gen, dex, caught):
    key = f'''legend_token_gen{gen}'''
    bundles = self._legend_bundles(gen)
    idx = (lambda .0: for None in .0:
    i = ()b = Noneif not int(b.get('dex', -1)) == int(dex):
    continuei)(enumerate(bundles)(), None)
    if idx is None:
        return None
    self.state[key] = bundles if bundles else None
