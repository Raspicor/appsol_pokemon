# module.PetApp.open_pokedex._update_legend_token_btn
# source line 16114
# Recovered from bytecode; default argument values are not shown.

def _update_legend_token_btn(d, status, entry):
    if bool(entry.get('legendary')) or status == 'caught':
        legend_token_btn.pack_forget()
        return None
    gen = None(d)
    bundle = self._legend_bundle_for_dex(gen, d)
    if bundle:
        legend_token_btn.configure(text = f'''⚔ 도전하기! (남은 {bundle.get('attempts_left', 0)}번)''')
    else:
        cost = int(round(SHOP_LEGEND_TOKEN_COST * SHOP_GEN_PRICE_MULT.get(gen, 1)))
        legend_token_btn.configure(text = f'''🔮 {gen}세대 전설조우 토큰 사기 (💰{cost}골드, {SHOP_LEGEND_TOKEN_COUNT}회권)''')
    legend_token_btn.pack(pady = (6, 0))
