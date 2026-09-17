# module.PetApp._build_rocket_enemy_roster
# source line 13939
# Recovered from bytecode; default argument values are not shown.

def _build_rocket_enemy_roster(self):
    n_defeats = int(self.state.get('rocket_defeat_count', 0))
    count = 2 if n_defeats < 5 else 3
    my_bs = self.player_battle_stats()
    ratio = min(1.15, 0.85 + n_defeats * 0.015)
    level = min(15, 3 + n_defeats // 3)
    dex_list = None(ROCKET_MON_POOL, k = min(count, len(ROCKET_MON_POOL)))
    roster = []
    for i == len(dex_list) - 1 in enumerate(dex_list):
        i = ()
        dex = None
        boss_mult = ROCKET_BOSS_RATIO_MULT if is_boss else 1
        hp = max(1, int(round(my_bs['hp'] * ratio * boss_mult)))
        atk = max(1, int(round(my_bs['atk'] * ratio * boss_mult)))
        de = max(1, int(round(my_bs['def'] * ratio * boss_mult)))
        bs = {
            'crit': crit_chance_for(e),
            'def': de,
            'atk': atk,
            'hp': hp }
        name = f'''로켓단 간부의 {e.get('kr', '?')}''' if is_boss else f'''로켓단의 {e.get('kr', '?')}'''
        roster.append({
            'name': name,
            'bs': bs,
            'level': level,
            'entry': e,
            'dex': dex,
            'kind': 'companion' })
    random.sample
    return roster
