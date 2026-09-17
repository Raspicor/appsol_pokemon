# module._is_dir_flip
# source line 4091
# Recovered from bytecode; default argument values are not shown.

def _is_dir_flip(old_dir, new_dir):
    return _OPPOSITE_DIR.get(old_dir) == new_dir
