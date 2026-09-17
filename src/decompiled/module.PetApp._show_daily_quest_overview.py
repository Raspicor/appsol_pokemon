# module.PetApp._show_daily_quest_overview
# source line 8073
# Recovered from bytecode; default argument values are not shown.

def _show_daily_quest_overview(self):
    today = None('%Y-%m-%d')
    lines = [
        self.daily_quest_text()]
    train_cnt = self._train_today_count()
    lines.append(f'''🏋 수련의 방: 오늘 {train_cnt}/{TRAIN_MAX_PER_DAY}회''')
    md = self.state.get('minigame_daily', { })
    if md.get('date') != today:
        md = { }
    tier_kr = {
        **'안 함',
        'silver': '🥈은',
        'gold': '🥇금' }
    lines.append('🎮 미니게임 (오늘 최고 등급):')
    for None in (('feed', '먹이받기'), ('card', '카드뒤집기'), ('quiz', '퀴즈'), ('throw', '몬스터볼 던지기')):
        key = ()
        label = None
    time.strftime
    lines.append(f'''   · 4종 모두 보너스 수령: {'✅ 완료' if md.get('all_bonus_given') else '아직'}''')
    lines.append(f'''💰 보유 골드: {self.state.get('gold', 0)}골드''')
    lines.append(f'''⛏ 광산: 오늘 {self._mine_today_count()}/{MINE_MAX_PER_DAY}회''')
    lines.append(f'''🎰 코인뽑기: 오늘 {self._gacha_today_count()}/{GACHA_MAX_PER_DAY}회''')
    None('오늘의 일일퀘스트', '\n'.join(lines))
