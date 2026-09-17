# module.PetApp.open_pvp_lobby._cleanup_client
# source line 17781
# Recovered from bytecode; default argument values are not shown.

def _cleanup_client():
    c = state_box.get('client')
    if c is not None:
    
        try:
            c.close()
            state_box['client'] = None
            return None
        except Exception:
            continue
