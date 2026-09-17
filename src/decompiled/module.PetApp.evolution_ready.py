# module.PetApp.evolution_ready
# source line 7557
# Recovered from bytecode; default argument values are not shown.

def evolution_ready(self):
    sp = SPECIES[self.state['starter']]
    stage = self.state.get('stage', 0)
    max_stage = 1 if sp.get('branching') else len(sp['stages']) - 1
    if stage >= max_stage:
        return False
    tier = sp['evolve_tiers'][stage] if None < len(sp['evolve_tiers']) else 1
    if not self.state.get('stage_started_at'):
        self.state.get('stage_started_at')
    started = None()
    elapsed_days = (None() - started) / 86400
    quota_days = self.state.get('quota_days_done', 0)
    if not elapsed_days >= BASE_PASSIVE_DAYS * tier:
        elapsed_days >= BASE_PASSIVE_DAYS * tier
    return quota_days >= BASE_QUOTA_DAYS * tier
