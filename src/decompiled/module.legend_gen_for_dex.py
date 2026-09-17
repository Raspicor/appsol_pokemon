# module.legend_gen_for_dex
# source line 1412
# Recovered from bytecode; default argument values are not shown.

def legend_gen_for_dex(dex):
    dex = int(dex)
    if dex >= GEN4_START_DEX:
        return 4
    if None >= GEN3_START_DEX:
        return 3
    if None >= GEN2_START_DEX:
        return 2
