# module.PetApp._check_inf_recurring_title
# source line 14847
# Recovered from bytecode; default argument values are not shown.

def _check_inf_recurring_title(self, cleared_stage):
    msgs = []
    if cleared_stage % INF_TITLE_EVERY == 0:
        n = cleared_stage // INF_TITLE_EVERY
        tid = f'''inf_stage_{cleared_stage}'''
        if cleared_stage == 400:
            label = '포켓몬 배틀 달인'
        elif cleared_stage == 800:
            label = '포켓몬 전투 마스터'
        elif n > 1:
            pass
    
        label = ' 👑' + ''
        msg = self._award_title(tid, label)
        if msg:
            msgs.append(msg)
    return msgs
