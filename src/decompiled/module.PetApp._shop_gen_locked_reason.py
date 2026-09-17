# module.PetApp._shop_gen_locked_reason
# source line 13114
# Recovered from bytecode; default argument values are not shown.

def _shop_gen_locked_reason(self, gen):
    if not gen == 2 and all_gen1_caught(self.state):
        return '1세대를 먼저 다 모아야 열려요'
    if not None == 3 and all_gen2_caught(self.state):
        return '2세대를 먼저 다 모아야 열려요'
    if not None == 4 and all_gen3_caught(self.state):
        return '3세대를 먼저 다 모아야 열려요'
