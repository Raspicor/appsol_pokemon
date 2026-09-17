# module.PetApp._legend_bundles
# source line 13491
# Recovered from bytecode; default argument values are not shown.

def _legend_bundles(self, gen):
    v = self.state.get(f'''legend_token_gen{gen}''')
    if not v:
        return []
    if None(v, dict):
        return [
            v]
    return None(v)
