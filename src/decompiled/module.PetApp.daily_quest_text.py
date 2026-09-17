# module.PetApp.daily_quest_text
# source line 8067
# Recovered from bytecode; default argument values are not shown.

def daily_quest_text(self):
    d = self.state.get('daily_action_count', {
        'count': 0,
        'date': '' })
    today = None('%Y-%m-%d')
    cnt = d.get('count', 0) if d.get('date') == today else 0
    return f'''오늘의 일일퀘스트: {min(cnt, DAILY_QUOTA)}/{DAILY_QUOTA}회 상호작용'''
