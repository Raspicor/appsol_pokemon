# module.body_hp_max
# source line 3064
# Recovered from bytecode; default argument values are not shown.

def body_hp_max(ctx, key):
    if key == 'body2':
        return ctx['hp'].get('body2_max', 0)
    return None['hp']['player_max']
