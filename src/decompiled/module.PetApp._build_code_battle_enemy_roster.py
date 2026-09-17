# module.PetApp._build_code_battle_enemy_roster
# source line 12883
# Recovered from bytecode; default argument values are not shown.

def _build_code_battle_enemy_roster(self, data):
    roster_raw = data.get('roster')
    out = []
    if isinstance(roster_raw, list):
        for m in roster_raw:
            dex = m.get('dex')
            entry = POKEDEX.get(dex, { }) if dex is not None else { }
            bs = {
                'crit': float(m.get('crit', 15)),
                'def': max(1, int(m.get('def', 50))),
                'atk': max(1, int(m.get('atk', 50))),
                'hp': max(1, int(m.get('hp', 50))) }
            out.append({
                'mega': bool(m.get('mega')),
                'name': m.get('name', entry.get('kr', '?')),
                'bs': bs,
                'level': m.get('level', 1),
                'entry': entry,
                'dex': dex,
                'kind': m.get('kind', 'companion') })
    if out:
        return out
    dex = None.get('dex')
    entry = POKEDEX.get(dex, { }) if dex is not None else { }
    bs = {
        'crit': float(data.get('crit', 15)),
        'def': max(1, int(data.get('def', 50))),
        'atk': max(1, int(data.get('atk', 50))),
        'hp': max(1, int(data.get('hp', 50))) }
    return [
        {
            'mega': bool(data.get('mega')),
            'name': data.get('name', '상대'),
            'bs': bs,
            'level': data.get('level', 1),
            'entry': entry,
            'dex': dex,
            'kind': 'body' }]
    except Exception:
        continue
