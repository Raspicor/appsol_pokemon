# module.all_title_defs
# source line 2495
# Recovered from bytecode; default argument values are not shown.

def all_title_defs():
    defs = [
        ('inf_stage_400', '무한성장 400스테이지 칭호', '아무 모드나 무한성장미터 400스테이지 클리어', False),
        ('inf_stage_800', '포켓몬 전투 마스터 (800스테이지)', '아무 모드나 무한성장미터 800스테이지 클리어', False),
        ('inf_stage_1200', '1200스테이지 칭호', '아무 모드나 무한성장미터 1200스테이지 클리어(1600, 2000...도 400의 배수마다 같은 방식으로 계속 나와요)', False)]
    for mode in INF_METER_MODES:
        for gen in range(1, 10):
            tid = master_title_id(mode, gen)
            gname = _TITLE_GEN_NAMES[gen]
            label = f'''{gname} {INF_MODE_MASTER_LABEL[mode]}'''
            cond = f'''{INF_MODE_MASTER_LABEL[mode]} 모드 {gen * 100}스테이지 + {gname} 도감 완성 + {gname} 체육관 뱃지 전부'''
            if gen > 4:
                cond += ' (5~9세대는 아직 게임에 없어서 지금은 딸 수 없어요)'
            defs.append((tid, label, cond, True))
        INF_METER_MODES
    for entry in NEW_TITLE_TABLE:
        defs.append((entry['id'], entry['label'], entry['cond_text'], bool(entry.get('equip'))))
    return _sort_titles_top_priority(defs, (lambda d: d[0]))
