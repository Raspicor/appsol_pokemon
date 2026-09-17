# module.mega_companion_ready
# source line 504
# Recovered from bytecode; default argument values are not shown.

def mega_companion_ready(dex, caught):
    if not mega_companion_eligible_species(dex):
        return False
    if not None:
        pass
    caught = { }
    info = caught.get(str(int(dex)))
    lv = info.get('level', 0) if isinstance(info, dict) else 0

    try:
        return int(lv) >= MEGA_COMPANION_LEVEL_REQUIRE
    except Exception:
        return False
