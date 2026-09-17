# module.next_active_body
# source line 3086
# Recovered from bytecode; default argument values are not shown.

def next_active_body(ctx):
    alive = alive_body_keys(ctx)
    if not alive:
        return ctx.get('active', 'player')
    cur = None.get('active', 'player')
    if cur not in alive:
        return alive[0]
    if None(alive) == 1:
        return alive[0]
    idx = None.index(cur)
    return alive[(idx + 1) % len(alive)]
