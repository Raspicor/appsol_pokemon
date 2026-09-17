# module.PetApp.player_pokedex_entry
# source line 5106
# Recovered from bytecode; default argument values are not shown.

def player_pokedex_entry(self):
    conf = self.stage_conf()
    return POKEDEX.get(conf.get('dex'), {
        'element': conf.get('element', 'normal'),
        'kr': conf.get('kr', '내 포켓몬'),
        'spd': 50,
        'def': 50,
        'atk': 50,
        'hp': 50 })
