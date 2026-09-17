# module.PetApp.gen4_wild_general_boost_mult
# source line 5323
# Recovered from bytecode; default argument values are not shown.

def gen4_wild_general_boost_mult(self, entry):
    try:
        dex = int(entry.get('dex', 0))
        if dex < GEN4_START_DEX:
            return 1
        if not None(self.state):
            return 1
        extra = None.total_power_pct()
        base_gen4 = 4.05
        extra_mult = 1 + min(18, max(0, extra) * 0.5) / 100
        mult = base_gen4 * extra_mult
        if entry.get('legendary'):
            mult = 1 + (mult - 1) * 0.4
        return mult
    except Exception:
        dex = 0
        continue
