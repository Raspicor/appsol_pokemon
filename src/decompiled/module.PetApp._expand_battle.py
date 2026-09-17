# module.PetApp._expand_battle
# source line 10408
# Recovered from bytecode; default argument values are not shown.

def _expand_battle(self, ctx):
    if not ctx['flags']['started']:
        self._build_precombat_full(ctx)
        return None
    None._build_combat_full(ctx)
