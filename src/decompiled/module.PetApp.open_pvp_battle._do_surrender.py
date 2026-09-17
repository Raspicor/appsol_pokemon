# module.PetApp.open_pvp_battle._do_surrender
# source line 18134
# Recovered from bytecode; default argument values are not shown.

def _do_surrender():
    if b['ended']:
        return None

    try:
        client.send({
            'type': 'surrender' })
        None(False, '내가 항복했어요.')
        return None
    except Exception:
        continue
