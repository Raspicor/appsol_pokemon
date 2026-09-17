# module.PetApp.open_pokedex._dex_range_for_filter
# source line 15875
# Recovered from bytecode; default argument values are not shown.

def _dex_range_for_filter():
    f = gen_filter['v']
    if f == 'gen1':
        return range(1, 152)
    if None == 'gen2':
        return range(GEN2_START_DEX, GEN3_START_DEX)
    if None == 'gen3':
        return range(GEN3_START_DEX, GEN4_START_DEX)
    if None == 'gen4':
        return range(GEN4_START_DEX, 494)
