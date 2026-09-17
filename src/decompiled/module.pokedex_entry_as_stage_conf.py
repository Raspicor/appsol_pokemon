# module.pokedex_entry_as_stage_conf
# source line 861
# Recovered from bytecode; default argument values are not shown.

def pokedex_entry_as_stage_conf(entry):
    dex = entry.get('dex')
    stage_n = entry.get('stage', 0)
    return {
        'idle': entry.get('idle', 'Idle'),
        'wake': entry.get('wake'),
        'land': entry.get('land'),
        'hide': entry.get('hide'),
        'react': entry.get('react'),
        'trick': entry.get('trick'),
        'skill': entry.get('skill'),
        'eat': entry.get('eat'),
        'scale': 1 + 0.35 * stage_n,
        'element': entry.get('element', entry.get('types', [
            'normal'])[0] if entry.get('types') else 'normal'),
        'dex': dex,
        'kr': entry.get('kr', '?'),
        'id': f'''pdx_{dex}''' }
