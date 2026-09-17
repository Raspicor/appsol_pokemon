# module.PetApp.evolution_progress_text
# source line 7957
# Recovered from bytecode; default argument values are not shown.

def evolution_progress_text(self):
    sp = SPECIES[self.state['starter']]
    stage = self.state.get('stage', 0)
    max_stage = 1 if sp.get('branching') else len(sp['stages']) - 1
    if stage >= max_stage:
        return '최종 진화 완료'
    tier = sp['evolve_tiers'][stage] if None < len(sp['evolve_tiers']) else 1
    if not self.state.get('stage_started_at'):
        self.state.get('stage_started_at')
    started = None()
    elapsed_days = (None() - started) / 86400
    quota_days = self.state.get('quota_days_done', 0)
    txt = f'''방치 {elapsed_days:.1f}/{BASE_PASSIVE_DAYS * tier}일  또는  일일퀘스트 완료 {quota_days}/{BASE_QUOTA_DAYS * tier}일'''
    if self.evolution_ready():
        txt += "  (✅ 진화 가능! '🧬 진화/레벨 탭'에서 진화시켜보세요)"
    return txt
