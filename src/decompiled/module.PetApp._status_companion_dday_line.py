# module.PetApp._status_companion_dday_line
# source line 8018
# Recovered from bytecode; default argument values are not shown.

def _status_companion_dday_line(self, d):
    try:
        dd = int(d)
        entry = POKEDEX.get(dd)
        if not entry:
            return None
        name = None.get('kr', '?')
        cur_level = self.state.get('caught', { }).get(str(dd), { }).get('level', 1)
    
        try:
            status = self.companion_evolution_status(dd)
            if not status.get('evolvable'):
                evo_txt = '진화없음'
            else:
            
                try:
                    if status.get('ready'):
                    
                        try:
                            evo_txt = '진화 가능!'
                        try:
                            if not status.get('timer_started'):
                            
                                try:
                                    evo_txt = '대기중'
                                try:
                                    remain_days = max(0, status.get('days_needed', 0) - status.get('elapsed_days', 0))
                                    evo_txt = f'''D-{remain_days:.1f}일'''
                                
                                    try:
                                        remain_n = self.companion_level_remaining_n(dd)
                                        if remain_n is None:
                                            lvl_txt = '레벨업 최고'
                                        else:
                                        
                                            try:
                                                if remain_n <= 0:
                                                    lvl_txt = '레벨업 가능!'
                                                else:
                                                
                                                    try:
                                                        lvl_txt = f'''레벨업 {remain_n}마리남음'''
                                                        return f'''🤝 {name}(Lv.{cur_level}) 진화 {evo_txt}, {lvl_txt}'''
                                                        except Exception:
                                                            return None
                                                        except Exception:
                                                            evo_txt = '?'
                                                            continue
                                                    except Exception:
                                                        lvl_txt = '?'
                                                        continue
