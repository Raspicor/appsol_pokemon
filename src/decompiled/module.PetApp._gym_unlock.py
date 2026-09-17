# module.PetApp._gym_unlock
# source line 17293
# Recovered from bytecode; default argument values are not shown.

def _gym_unlock(self, gctx):
    flags = gctx['flags']
    if flags['ended']:
        return None
    flags['locked'] = None
    if gctx['ui'].get('set_locked'):
        None(False)
    if gctx['ui'].get('refresh_ult'):
        None()
        return None
    return gctx['ui']['set_locked']
