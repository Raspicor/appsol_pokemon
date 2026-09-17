# module.PetApp._inf_build_enemy_roster
# source line 14329
# Recovered from bytecode; default argument values are not shown.

def _inf_build_enemy_roster(self, mode, stage):
    cycle = ()
    gen = inf_stage_cycle_info(stage)
    pos_in_block = None
    _pos_in_cycle = None
    level = ()
    mult = inf_stage_level_and_mult(stage, mode)
    (lambda g: pool = list(LEGENDARY_DEX_BY_GEN.get(g, []))if not pool:
    pool = (lambda .0: for None in .0:
    d = ()e = Noneif not e.get('legendary'):
    continued)(POKEDEX.items()())
        return pool
    ) = _inf_ult_def_bonus(mode)
    if kind == 'mirror':
        my_roster = self._inf_build_player_roster(mode)
        mirror_entry = self.player_pokedex_entry()
        src_bs = my_roster[0]['bs']
        if gen == 4:
            pass
        elif gen == 3:
            pass
    
        mirror_self_mult = 1
        roster = [
            {
                'mega': my_roster[0].get('mega', False),
                'name': f'''거울 속 {self.display_name()}''',
                'bs': mirror_bs,
                'level': my_roster[0]['level'],
                'entry': mirror_entry,
                'dex': self.player_dex(),
                'kind': 'body' }]
        legends = None(gen)
        None(legends)
        picked = legends[:max(1, companion_slot_count(self.state))]
        for d in picked:
            e = POKEDEX.get(d, { })
            bs = battle_stats(e, level, mega_mult = mult, def_pct = ult_def_bonus)
            roster.append({
                'name': e.get('kr', '?'),
                'bs': dict(bs),
                'level': level,
                'entry': e,
                'dex': d,
                'kind': 'companion' })
        random.shuffle
        return roster
    if inf_stage_kind(pos_in_block) == 'boss':
        legends = None(gen)
        None(legends)
        picked = legends[<TYPE: 58>
    ]
        roster = []
        for d in picked:
            e = POKEDEX.get(d, { })
            bs = battle_stats(e, level, mega_mult = mult, def_pct = ult_def_bonus)
            roster.append({
                'name': e.get('kr', '?'),
                'bs': dict(bs),
                'level': level,
                'entry': e,
                'dex': d,
                'kind': 'companion' })
        random.shuffle
        return roster
    if None == 'free':
        if pos_in_block < 34:
            pass
        elif pos_in_block < 67:
            pass
    
        n = 3
        if all_gen3_caught(self.state):
            pass
        elif all_gen2_caught(self.state):
            pass
        elif all_gen1_caught(self.state):
            pass
    
        hi_gen_unlocked = 1
        hi = gen_dex_range(hi_gen_unlocked)[1]
        lo = 1
        for d, e in :
            if  <= lo, d:
                if not lo, d < hi:
                    continue
                else:
                
                if e.get('legendary'):
                    continue
    
        , [], pool, d = POKEDEX.items(), d, e
        e = 2
        if not pool:
            if not list(POKEDEX.keys())[<TYPE: 58>
    ]:
                list(POKEDEX.keys())[<TYPE: 58>
    ]
            pool = [
                1]
        for None in :
            pass
        random.choice
        None = 
        _ = , []
        roster = []
        for d in dex_list:
            e = POKEDEX.get(d, { })
            bs = battle_stats(e, level, mega_mult = mult, def_pct = ult_def_bonus)
            roster.append({
                'name': e.get('kr', '?'),
                'bs': dict(bs),
                'level': level,
                'entry': e,
                'dex': d,
                'kind': 'companion' })
        range(n), _
        return roster
    if None == 'type':
        my_roster = self._inf_build_player_roster(mode)
        (dex, is_repeat) = self._inf_pick_type_biased_dex(gen, pos_in_block, my_roster)
    else:
        (dex, is_repeat) = _inf_normal_species_for_stage(gen, pos_in_block)
    if dex is None:
        dex = 1
        is_repeat = False
    e = POKEDEX.get(dex, { })
    bs = battle_stats(e, level, mega_mult = mult, def_pct = ult_def_bonus)
    nm = '강해져서 돌아온 ' + e.get('kr', '?') if is_repeat else e.get('kr', '?')
    return [
        {
            'name': nm,
            'bs': dict(bs),
            'level': level,
            'entry': e,
            'dex': dex,
            'kind': 'companion' }]
