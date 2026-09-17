# module._species_strength_score
# source line 1655
# Recovered from bytecode; default argument values are not shown.

def _species_strength_score(entry):
    return entry.get('hp', 50) + entry.get('atk', 50) + entry.get('def', 50)
