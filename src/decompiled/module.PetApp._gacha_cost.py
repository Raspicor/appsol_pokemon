# module.PetApp._gacha_cost
# source line 13126
# Recovered from bytecode; default argument values are not shown.

def _gacha_cost(self, gen):
    return int(round(SHOP_GACHA_COST * SHOP_GEN_PRICE_MULT.get(gen, 1)))
