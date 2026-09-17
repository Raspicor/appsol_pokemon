# module.PetApp._earn_gold
# source line 14786
# Recovered from bytecode; default argument values are not shown.

def _earn_gold(self, amount, source):
    amt = int(amount)
    if amt <= 0:
        return []
    mult = None + title_gold_mult_pct(self.state) / 100
    if source == 'catch':
        mult += title_gold_catch_bonus_pct(self.state) / 100
    elif source == 'mine':
        mult += title_mine_reward_pct(self.state) / 100
    final_amt = max(1, int(round(amt * mult)))
    if source == 'catch':
        final_amt += int(title_mine_win_gold_flat(self.state))
    self.state['gold'] = int(self.state.get('gold', 0)) + final_amt
    self.state['gold_earned_total'] = int(self.state.get('gold_earned_total', 0)) + final_amt
    return self._check_new_titles()
