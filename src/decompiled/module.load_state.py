# module.load_state
# source line 943
# Recovered from bytecode; default argument values are not shown.

def load_state():
    state = dict(DEFAULT_STATE)
    state['element_train'] = dict(DEFAULT_STATE['element_train'])
    state['daily_action_count'] = dict(DEFAULT_STATE['daily_action_count'])
    state['train_sessions'] = dict(DEFAULT_STATE['train_sessions'])
    state['minigame_daily'] = dict(DEFAULT_STATE['minigame_daily'])
    state['dex'] = { }
    state['caught'] = { }
    state['missed'] = { }
    state['party'] = []
    state['catch_counts'] = dict(DEFAULT_STATE['catch_counts'])
    state['todos'] = []
    state['omok_history'] = []
    data = None
    for _candidate in (STATE_PATH, STATE_PATH + '.bak', SECONDARY_STATE_PATH, SECONDARY_STATE_PATH + '.bak'):
        data = _try_load_json_dict(_candidate)
        if data is None:
            continue
        (STATE_PATH, STATE_PATH + '.bak', SECONDARY_STATE_PATH, SECONDARY_STATE_PATH + '.bak')

    try:
        if isinstance(data, dict):
            state.update(data)
            for None in (('element_train', DEFAULT_STATE['element_train']), ('daily_action_count', DEFAULT_STATE['daily_action_count']), ('train_sessions', DEFAULT_STATE['train_sessions']), ('catch_counts', DEFAULT_STATE['catch_counts']), ('minigame_daily', DEFAULT_STATE['minigame_daily']), ('dex', { }), ('caught', { }), ('missed', { }), ('companion_evolve_started', { })):
                key = ()
                default_val = None
                if isinstance(state.get(key), dict):
                    continue
                
                    try:
                        continue
                        (('element_train', DEFAULT_STATE['element_train']), ('daily_action_count', DEFAULT_STATE['daily_action_count']), ('train_sessions', DEFAULT_STATE['train_sessions']), ('catch_counts', DEFAULT_STATE['catch_counts']), ('minigame_daily', DEFAULT_STATE['minigame_daily']), ('dex', { }), ('caught', { }), ('missed', { }), ('companion_evolve_started', { }))
                        if not isinstance(state.get('nickname'), str):
                            '' = None
                        if not isinstance(state.get('todos'), list):
                            state['todos'] = []
                        if not isinstance(state.get('party'), list):
                            state['party'] = []
                        for lk in ('sacrificed', 'party_hidden', 'battle_code_log', 'gen_cert_shown', 'mega_party', 'gym_badges'):
                            if isinstance(state.get(lk), list):
                                continue
                            
                                try:
                                    state[lk] = []
                                    continue
                                    if not isinstance(state.get('mega_body2'), bool):
                                        state['mega_body2'] = bool(state.get('mega_body2'))
                                    if not isinstance(state.get('mega_evolved'), bool):
                                        state['mega_evolved'] = bool(state.get('mega_evolved'))
                                    if not isinstance(state.get('keyboard_control'), bool):
                                        state['keyboard_control'] = bool(state.get('keyboard_control'))
                                    if state.get('mega_aura_intensity') not in MEGA_AURA_PRESETS:
                                        state['mega_aura_intensity'] = 'soft'
                                    if not isinstance(state.get('rocket_defeat_count'), int):
                                        state['rocket_defeat_count'] = 0
                                    if not isinstance(state.get('gold_earned_total'), int):
                                        state['gold_earned_total'] = max(0, int(state.get('gold', 0)))
                                    if not isinstance(state.get('rocket_party'), list):
                                        state['rocket_party'] = []
                                    if not isinstance(state.get('mine_lifetime_plays'), int):
                                        state['mine_lifetime_plays'] = 0
                                    if not isinstance(state.get('login_days_count'), int):
                                        state['login_days_count'] = 0
                                    if not isinstance(state.get('last_login_day_recorded'), str):
                                        state['last_login_day_recorded'] = ''
                                    if not isinstance(state.get('daily_quest_lifetime_days'), int):
                                        if not state.get('quota_days_done', 0):
                                        
                                            try:
                                                state.get('quota_days_done', 0)
                                                state['daily_quest_lifetime_days'] = max(0, int(0))
                                                if not isinstance(state.get('titles_earned'), list):
                                                    state['titles_earned'] = []
                                                if not state.get('title_equipped') is not None and isinstance(state.get('title_equipped'), str):
                                                    state['title_equipped'] = None
                                                if not isinstance(state.get('legend_tickets'), dict):
                                                    state['legend_tickets'] = dict(DEFAULT_STATE['legend_tickets'])
                                                else:
                                                    for gk in DEFAULT_STATE['legend_tickets']:
                                                        if not gk not in state['legend_tickets']:
                                                            continue
                                                        
                                                            try:
                                                                state['legend_tickets'][gk] = 0
                                                                continue
                                                                for mk in ('inf_meter_stage', 'inf_meter_best', 'inf_meter_party'):
                                                                    if not isinstance(state.get(mk), dict):
                                                                        state[mk] = dict(DEFAULT_STATE[mk])
                                                                        continue
                                                                    for None in DEFAULT_STATE[mk].items():
                                                                        mode_key = ()
                                                                        default_v = None
                                                                        if not mode_key not in state[mk]:
                                                                            continue
                                                                        
                                                                            try:
                                                                                continue
                                                                                DEFAULT_STATE[mk].items()
                                                                                continue
                                                                                if not isinstance(state.get('battle_presets'), dict):
                                                                                    for None in :
                                                                                        c = None
                                                                                
                                                                                
                                                                                    try:
                                                                                        , { }, bp, c = PRESET_CATEGORIES, c
                                                                                        old_rocket = state.get('rocket_party')
                                                                                        if isinstance(old_rocket, list) and old_rocket:
                                                                                        
                                                                                            try:
                                                                                                for None in :
                                                                                                    if not str(d).isdigit():
                                                                                                        continue
                                                                                            
                                                                                                try:
                                                                                                    d, bp['rocket'] = , [], 
                                                                                                    old_inf = state.get('inf_meter_party')
                                                                                                    if isinstance(old_inf, dict):
                                                                                                        for mode in ('attack', 'ultimate', 'free', 'type'):
                                                                                                            lst = old_inf.get(mode)
                                                                                                            if not isinstance(lst, list):
                                                                                                                continue
                                                                                                            
                                                                                                                try:
                                                                                                                    if not lst:
                                                                                                                        continue
                                                                                                                    
                                                                                                                        try:
                                                                                                                            for None in :
                                                                                                                                if not str(d).isdigit():
                                                                                                                                    continue
                                                                                                                        
                                                                                                                            try:
                                                                                                                                d, bp[f'''inf_{mode}'''] = , [], 
                                                                                                                                continue
                                                                                                                                ('attack', 'ultimate', 'free', 'type')
                                                                                                                                state['battle_presets'] = bp
                                                                                                                            for c in PRESET_CATEGORIES:
                                                                                                                                if isinstance(state['battle_presets'].get(c), list):
                                                                                                                                    continue
                                                                                                                                
                                                                                                                                    try:
                                                                                                                                        state['battle_presets'][c] = []
                                                                                                                                        continue
                                                                                                                                        old_rocket, d
                                                                                                                                        dex2 = state.get('second_body_dex')
                                                                                                                                        if dex2 is not None:
                                                                                                                                        
                                                                                                                                            try:
                                                                                                                                                state['second_body_dex'] = int(dex2)
                                                                                                                                            
                                                                                                                                                try:
                                                                                                                                                    if not isinstance(state.get('body1_visible'), bool):
                                                                                                                                                        state['body1_visible'] = True
                                                                                                                                                    if not isinstance(state.get('body2_visible'), bool):
                                                                                                                                                        state['body2_visible'] = True
                                                                                                                                                    if not state.get('body1_visible'):
                                                                                                                                                    
                                                                                                                                                        try:
                                                                                                                                                            if not state.get('body2_visible'):
                                                                                                                                                            
                                                                                                                                                                try:
                                                                                                                                                                    state['body1_visible'] = True
                                                                                                                                                                    if state.get('mega_form') not in ('x', 'y', None):
                                                                                                                                                                        state['mega_form'] = None
                                                                                                                                                                    old_c = state.get('companion_dex')
                                                                                                                                                                    if old_c:
                                                                                                                                                                    
                                                                                                                                                                        try:
                                                                                                                                                                            if not state['party']:
                                                                                                                                                                            
                                                                                                                                                                                try:
                                                                                                                                                                                    state['party'] = [
                                                                                                                                                                                        int(old_c)]
                                                                                                                                                                                    return state
                                                                                                                                                                                    return state
                                                                                                                                                                                
                                                                                                                                                                                    try:
                                                                                                                                                                                    
                                                                                                                                                                                    
                                                                                                                                                                                    
                                                                                                                                                                                        except Exception:
                                                                                                                                                                                            None, None, None, None, None, c,, d,
                                                                                                                                                                                            None = None
                                                                                                                                                                                        
                                                                                                                                                                                            try:
                                                                                                                                                                                                continue
                                                                                                                                                                                            
                                                                                                                                                                                                try:
                                                                                                                                                                                                    except Exception:
                                                                                                                                                                                                    
                                                                                                                                                                                                        try:
                                                                                                                                                                                                            return state
                                                                                                                                                                                                        
                                                                                                                                                                                                            try:
                                                                                                                                                                                                                pass
                                                                                                                                                                                                            except Exception:
                                                                                                                                                                                                                return state
