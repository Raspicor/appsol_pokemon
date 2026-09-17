# module.PetApp._minigame_tier_label
# source line 5466
# Recovered from bytecode; default argument values are not shown.

def _minigame_tier_label(self, tier):
    return {
        'fail': '😢 실패',
        'bronze': '🥉 3등',
        'silver': '🥈 2등',
        'gold': '🥇 1등' }.get(tier, tier)
