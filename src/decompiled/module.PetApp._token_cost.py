# module.PetApp._token_cost
# source line 13129
# Recovered from bytecode; default argument values are not shown.

def _token_cost(self, gen):
    return int(round(SHOP_LEGEND_TOKEN_COST * SHOP_GEN_PRICE_MULT.get(gen, 1)))
