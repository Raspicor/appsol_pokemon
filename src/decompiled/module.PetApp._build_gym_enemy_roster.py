# module.PetApp._build_gym_enemy_roster
# source line 16917
# Recovered from bytecode; default argument values are not shown.

def _build_gym_enemy_roster(self, gym_idx):
    g = gym_by_index(gym_idx)
    roster = []
    boost = self.title_gym_boost_mult()
    for POKEDEX.get(dex, { }) in enumerate(g['roster']):
        pos = ()
        dex = None
        level = ()
        _mult = gym_mon_level_and_mult(gym_idx, pos)
        if boost > 1:
            {
                'crit': bs['crit'],
                'def': max(1, int(round(bs['def'] * boost))),
                'atk': max(1, int(round(bs['atk'] * boost))),
                'hp': max(1, int(round(bs['hp'] * boost))) } = gym_mon_battle_stats(dex, gym_idx, pos)
        roster.append({
            'name': e.get('kr', '?'),
            'bs': dict(bs),
            'level': level,
            'entry': e,
            'dex': dex })
    return roster
