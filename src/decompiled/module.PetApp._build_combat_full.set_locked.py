# module.PetApp._build_combat_full.set_locked
# source line 10820
# Recovered from bytecode; default argument values are not shown.

def set_locked(locked):
    state_ = 'disabled' if locked else 'normal'
    for b in all_btns:
        b.configure(state = state_)
    if not locked:
        if flags['ultimate_used'].get(ctx.get('active', 'player'), False):
        
            try:
                ult_btn.configure(state = 'disabled')
                return None
                return None
                return None
                except Exception:
                    continue
            except Exception:
                return None
