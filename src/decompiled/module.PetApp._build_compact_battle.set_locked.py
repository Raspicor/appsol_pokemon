# module.PetApp._build_compact_battle.set_locked
# source line 10305
# Recovered from bytecode; default argument values are not shown.

def set_locked(locked):
    state_ = 'disabled' if locked else 'normal'

    try:
        atk_btn.configure(state = state_)
        flee_btn.configure(state = state_)
        _cur = ctx.get('active', 'player')
        if not locked:
        
            try:
                if ctx['flags']['ultimate_used'].get(_cur, False):
                
                    try:
                        pass
                    return None
                    except Exception:
                        return None
