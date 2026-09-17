# module.PetApp._code_battle_finish
# source line 13086
# Recovered from bytecode; default argument values are not shown.

def _code_battle_finish(self, gctx, won, conceded):
    flags = gctx['flags']
    if flags['ended']:
        return None
    flags['ended'] = None
    flags['locked'] = True
    win = gctx['win']
    opp_name = gctx.get('opp_name', '상대')
    result = '승리' if won else '패배'
    'opponent'({
        time.strftime: None('%Y-%m-%d %H:%M'),
        '기권' if not conceded and won else result: 'when',
        opp_name: 'result' })
    self.state['battle_code_log'] = self.state['battle_code_log'][-30:]
    self.save_state()

    try:
        win.destroy()
        if won:
            None('코드 대결 결과', f'''🎉 승리! {opp_name}을(를) 이겼어요!''')
            return None
        if self.state.setdefault('battle_code_log', []).append:
            None('코드 대결 결과', f'''{opp_name}과(와)의 대결을 기권했어요.''')
            return None
        None('코드 대결 결과', f'''패배... {opp_name}에게 졌어요. 팀을 더 키워서 다시 도전해보세요!''')
        return None
    except Exception:
        continue
