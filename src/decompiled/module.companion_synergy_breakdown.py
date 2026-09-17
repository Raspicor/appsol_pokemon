# module.companion_synergy_breakdown
# source line 2862
# Recovered from bytecode; default argument values are not shown.

def companion_synergy_breakdown(party_dex_list, caught, mega_party):
    rows = []
    if not caught:
        caught
    caught = { }
    mega_set = set()
    if not mega_party:
        mega_party
    for x in []:
        mega_set.add(int(x))
    if not party_dex_list:
        party_dex_list
    for d in []:
        e = POKEDEX.get(int(d))
        if not e:
            continue
        lv = 1
        info = caught.get(str(int(d)))
        if isinstance(info, dict):
            lv = int(info.get('level', 1))
        mult = companion_level_multiplier(lv)
        atk_c = (e.get('atk', 50) / 400) * 8
        def_c = (e.get('def', 50) / 400) * 8
        crit_c = (e.get('spd', 50) / 400) * 5
        t = e.get('element')
        if t in OFFENSIVE_TYPES:
            atk_c += 2
        if t in DEFENSIVE_TYPES:
            def_c += 2
        if t in FAST_TYPES:
            crit_c += 2
        atk_c *= mult
        def_c *= mult
        crit_c *= mult
        gen_mult = COMPANION_GEN_SYNERGY_MULT.get(legend_gen_for_dex(int(d)), 1)
        is_legendary = bool(e.get('legendary'))
        if is_legendary:
            gen_mult *= COMPANION_LEGENDARY_SYNERGY_MULT
        gen_mult *= LEGENDARY_SIGNATURE_TIER_MULT.get(int(d), 1)
        atk_c *= gen_mult
        def_c *= gen_mult
        crit_c *= gen_mult
        if int(d) == ARCEUS_DEX:
            atk_c = ARCEUS_EQUIP_ATK_PCT_AT_LV15 * (mult / companion_level_multiplier(15))
        if int(d) in mega_set:
            int(d) in mega_set
        is_mega = mega_companion_ready(d, caught)
        if is_mega:
            atk_c *= MEGA_COMPANION_STAT_MULT
            def_c *= MEGA_COMPANION_STAT_MULT
            crit_c *= MEGA_COMPANION_STAT_MULT
        rows.append({
            'crit_pct': crit_c,
            'def_pct': def_c,
            'atk_pct': atk_c,
            'gen_mult': gen_mult,
            'legendary': is_legendary,
            'mega': is_mega,
            'level_mult': mult,
            'level': lv,
            'element': e.get('element', 'normal'),
            'kr': e.get('kr', '?'),
            'dex': int(d) })
    return rows
    except Exception:
        continue
    except Exception:
        e = None
        continue
    except Exception:
        lv = 1
        continue
