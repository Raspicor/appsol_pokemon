# module.PetApp._start_gym_challenge
# source line 16881
# Recovered from bytecode; default argument values are not shown.

def _start_gym_challenge(self, gym_idx, fun_mode):
    g = gym_by_index(gym_idx)
    if not g or gym_challengeable(self.state, gym_idx):
        return None
    None._open_gym_battle_window(gym_idx, fun_mode = fun_mode)
