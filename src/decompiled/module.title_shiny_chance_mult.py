# module.title_shiny_chance_mult
# source line 2137
# Recovered from bytecode; default argument values are not shown.

def title_shiny_chance_mult(state):
    mult = 1
    earned_ids = _earned_ids(state)
    if 'shiny_hunter' in earned_ids:
        mult *= 1.5
        if title_equipped_id(state) == 'shiny_hunter':
            mult *= 4
    return mult
