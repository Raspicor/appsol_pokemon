# module.PetApp.open_infinite_stone._update_status
# source line 5826
# Recovered from bytecode; default argument values are not shown.

def _update_status():
    if state_holder['broken']:
        status_var.set('🎉 무한의 돌 시즌1 클리어! 돌이 완전히 부서졌어요.\n다음 시즌은 업데이트 예정입니다.')
        return None
    _next_milestone_text(None())
