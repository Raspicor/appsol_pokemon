# module.companion_synergy_bonus
# source line 2932
# Recovered from bytecode; default argument values are not shown.

def companion_synergy_bonus(party_dex_list, caught, mega_party):
    rows = companion_synergy_breakdown(party_dex_list, caught, mega_party)
    atk_pct = (lambda .0: for None in .0:
    r = Noner['atk_pct'])(rows())
    def_pct = (lambda .0: for None in .0:
    r = Noner['def_pct'])(rows())
    crit_pct = (lambda .0: for None in .0:
    r = Noner['crit_pct'])(rows())
    return (atk_pct, def_pct, crit_pct)
