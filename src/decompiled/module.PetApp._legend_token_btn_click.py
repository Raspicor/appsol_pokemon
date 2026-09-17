# module.PetApp._legend_token_btn_click
# source line 13528
# Recovered from bytecode; default argument values are not shown.

def _legend_token_btn_click(self, dex_win, dex, refresh_cb):
    if dex is None:
        return None
    dex = None(dex)
    gen = legend_gen_for_dex(dex)
    bundle = self._legend_bundle_for_dex(gen, dex)
    if bundle:
        entry = POKEDEX.get(dex)
        if not entry:
            return None
        None.open_battle(entry, int(bundle.get('level', 5)), legend_token_gen = gen)
        return None
    None._buy_legend_token(gen, refresh_cb)
