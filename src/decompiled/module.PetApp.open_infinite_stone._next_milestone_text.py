# module.PetApp.open_infinite_stone._next_milestone_text
# source line 5819
# Recovered from bytecode; default argument values are not shown.

def _next_milestone_text():
    cur = self.state.get('infinite_stone_damage', 0)
    for None in INFINITE_STONE_MILESTONES:
        threshold = ()
        tid = None
        if not cur < threshold:
            continue
        return '다음 목표: ', f'''{label} (앞으로 {None(threshold - cur)} 더!)'''
    return '모든 단계를 달성했어요!'
