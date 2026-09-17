# module.PetApp.battle_bodies_conf
# source line 5377
# Recovered from bytecode; default argument values are not shown.

def battle_bodies_conf(self):
    bodies = [
        {
            'dex': self.player_dex(),
            'is_starter': True,
            'level': self.body1_effective_level(),
            'entry': self.player_pokedex_entry(),
            'label': '1번 본체',
            'key': 'p1' }]
    dex2 = second_body_equipped_dex(self.state)
    if dex2:
        e2 = POKEDEX.get(int(dex2))
        if e2:
            lv2 = self.player_level()
            bodies.append({
                'dex': int(dex2),
                'is_starter': False,
                'level': lv2,
                'entry': e2,
                'label': '2번 본체',
                'key': 'p2' })
    return bodies
