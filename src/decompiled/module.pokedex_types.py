# module.pokedex_types
# source line 3174
# Recovered from bytecode; default argument values are not shown.

def pokedex_types(entry):
    if not entry:
        return [
            'normal']
    types = None.get('types')
    if types:
        return list(types)
    t = None.get('element')
    if t:
        return [
            t]
    return [
        None]
