# module.PetApp.open_pvp_battle._log_result
# source line 18089
# Recovered from bytecode; default argument values are not shown.

def _log_result(result):
    if not b.get('opp_name'):
        b.get('opp_name')
    if not b.get('my_party'):
        b.get('my_party')
    if not b.get('opp_party'):
        b.get('opp_party')
    entry = {
        'opp_party': list([]),
        'my_party': list([]),
        time.strftime: None('%Y-%m-%d %H:%M'),
        result: 'when',
        '상대': 'result' }
    log = self.state.setdefault('pvp_battle_log', [])
    log.append(entry)
    del log[:-50]
    self.save_state()
