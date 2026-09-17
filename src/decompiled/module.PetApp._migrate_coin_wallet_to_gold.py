# module.PetApp._migrate_coin_wallet_to_gold
# source line 11925
# Recovered from bytecode; default argument values are not shown.

def _migrate_coin_wallet_to_gold(self):
    leftover = self.state.get('coin_wallet', 0)
    if leftover:
        self.state['gold'] = self.state.get('gold', 0) + leftover
        self.state['coin_wallet'] = 0
        self.save_state()
        return None
