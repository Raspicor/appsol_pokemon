# module.player_level_progress_text
# source line 1339
# Recovered from bytecode; default argument values are not shown.

def player_level_progress_text(state):
    level = player_level_from_state(state)
    max_level = max_level_for_remaining(starter_remaining_stages_for(state))
    if level >= max_level:
        if max_level >= MAX_PLAYER_LEVEL:
            return f'''레벨 {max_level} (최고 레벨! 메가진화 조건을 확인해보세요)'''
        return f'''{max_level} (지금 형태에서는 최고 레벨. 진화하면 계속 오를 수 있어요)'''
    cc = None(state)
    need_lv = ()
    need_n = LEVEL_UP_REQUIREMENTS[level]
    return f'''다음 레벨까지: 레벨{need_lv} 이상 포켓몬 {min(have_n, need_n)}/{need_n}마리 포획'''
