# module.PetApp._status_body_dday_line
# source line 7973
# Recovered from bytecode; default argument values are not shown.

def _status_body_dday_line(self):
    try:
        name = self.display_name()
        level = player_level_from_state(self.state)
    
        try:
            if self.evolution_ready():
            
                try:
                    evo_txt = '진화 가능!'
                try:
                    sp = SPECIES[self.state['starter']]
                    stage = self.state.get('stage', 0)
                    if sp.get('branching'):
                    
                        try:
                            pass
                        max_stage = len(sp['stages']) - 1
                        if stage >= max_stage:
                            evo_txt = '진화 완료'
                        else:
                        
                            try:
                                tier = sp['evolve_tiers'][stage] if stage < len(sp['evolve_tiers']) else 1
                                if not self.state.get('stage_started_at'):
                                
                                    try:
                                        self.state.get('stage_started_at')
                                        started = None()
                                        elapsed_days = (None() - started) / 86400
                                        remain_days = max(0, BASE_PASSIVE_DAYS * tier - elapsed_days)
                                        evo_txt = f'''D-{remain_days:.1f}일'''
                                    
                                        try:
                                            max_level = max_level_for_remaining(self.starter_remaining_stages())
                                            if level >= max_level:
                                                lvl_txt = '레벨업 최고'
                                            else:
                                            
                                                try:
                                                    req = LEVEL_UP_REQUIREMENTS.get(level)
                                                    if req:
                                                    
                                                        try:
                                                            need_lv = ()
                                                            need_n = req
                                                            int(cc.get(str(need_lv), 0)) = ensure_catch_counts(self.state)
                                                            remain_n = max(0, need_n - have_n)
                                                            lvl_txt = f'''레벨업 {remain_n}마리남음''' if remain_n > 0 else '레벨업 가능!'
                                                        try:
                                                            lvl_txt = '?'
                                                            return f'''🏠 {name}(Lv.{level}) 진화 {evo_txt}, {lvl_txt}'''
                                                            except Exception:
                                                                time.time
                                                                return '🏠 (정보 없음)'
                                                            except Exception:
                                                                time.time
                                                                evo_txt = '?'
                                                                continue
                                                        except Exception:
                                                            time.time
                                                            lvl_txt = '?'
                                                            continue
