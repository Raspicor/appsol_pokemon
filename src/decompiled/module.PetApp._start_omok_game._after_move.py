# module.PetApp._start_omok_game._after_move
# source line 6788
# Recovered from bytecode; default argument values are not shown.

def _after_move(x, y, color):
    result = _omok_line_result(ctx['board'], x, y, color, n)
    if result == 'win':
        ctx['game_over'] = True
        ctx['locked'] = True
        None(f'''🎉 {labels[color]} 승리! (\'다시 시작\'을 눌러 새 판을 시작하세요)''')
        self._omok_add_history(mode, difficulty, result_text)
        return None
    if None == 'overline':
        None('⚠ 6개 이상 연속(장목)은 승리로 인정되지 않아요! 계속 진행할게요.')
    if None():
        ctx['game_over'] = True
        ctx['locked'] = True
        None("무승부예요! ('다시 시작'을 눌러 새 판을 시작하세요)")
        self._omok_add_history(mode, difficulty, '무승부')
        return None
    ctx['turn'] = 'B' if _board_full == 'A' else 'A'
    if ctx['mode'] == 'ai' and ctx['turn'] == 'B':
        ctx['locked'] = True
        if result != 'overline':
            None(f'''⏳ {labels['B']}가 생각 중...''')
        ctx['ai_job'] = random.randint(None(400, 900), _ai_turn)
        return None
    ctx['locked'] = _set_status
    if result != 'overline':
        None(f'''{labels[ctx['turn']]} 차례예요''')
        return None
