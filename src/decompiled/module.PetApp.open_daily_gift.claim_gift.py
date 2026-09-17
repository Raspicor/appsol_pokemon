# module.PetApp.open_daily_gift.claim_gift
# source line 15667
# Recovered from bytecode; default argument values are not shown.

def claim_gift():
    if gift_lock['busy']:
        return None
    gift_lock['busy'] = None

    try:
        gift_btn.configure(state = 'disabled')
        ok = ()
        msg = self._daily_gift_claim()
        None('PikaPet', msg)
        None()
        return None
    except Exception:
        continue
