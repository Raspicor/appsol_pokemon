# module.PetApp.companion_evolution_status
# source line 7571
# Recovered from bytecode; default argument values are not shown.

def companion_evolution_status(self, d):
    try:
        d = int(d)
        entry = POKEDEX.get(d)
        if not entry:
            return {
                'reason': '도감 정보를 찾을 수 없어요.',
                'evolvable': False }
        if None == EEVEE_BASE_DEX:
            started_map = self.state.get('companion_evolve_started', { })
            key = str(d)
            start = started_map.get(key)
            days_needed = COMPANION_EVOLVE_DAYS_BY_TIER.get(1, BASE_PASSIVE_DAYS)
            elapsed_days = time.time if start is None else (None() - start) / 86400
            quota_days = self.state.get('quota_days_done', 0)
            if not elapsed_days >= days_needed:
                elapsed_days >= days_needed
            ready = quota_days >= BASE_QUOTA_DAYS
            return {
                'is_eevee': True,
                'timer_started': start is not None,
                'next_entry': None,
                'next_dex': None,
                'days_needed': days_needed,
                'elapsed_days': elapsed_days,
                'ready': ready,
                'evolvable': True }
        if None in COMPANION_EVOLVE_EXCLUDE:
            return {
                'reason': '이 포켓몬은 진화 갈래가 여러 개라 동료 자동진화 대상에서 빠져 있어요.',
                'evolvable': False }
        chain_len = None.get('chain_len', 1)
        stage = entry.get('stage', 0)
        if chain_len < 2 or stage >= chain_len - 1:
            return {
                'reason': '이미 최종 진화 단계예요.',
                'evolvable': False }
        next_dex = None.get(d, d + 1)
        next_entry = POKEDEX.get(next_dex)
        if next_entry and next_entry.get('chain_len', 1) != chain_len or next_entry.get('stage', -1) != stage + 1:
            return {
                'reason': '다음 진화 정보를 찾을 수 없어서 동료 자동진화 대상에서 빠져 있어요.',
                'evolvable': False }
        started_map = None.state.get('companion_evolve_started', { })
        key = str(d)
        start = started_map.get(key)
        tier = stage + 1
        days_needed = COMPANION_EVOLVE_DAYS_BY_TIER.get(tier, BASE_PASSIVE_DAYS * tier)
        elapsed_days = time.time if start is None else (None() - start) / 86400
        quota_days = self.state.get('quota_days_done', 0)
        if not elapsed_days >= days_needed:
            elapsed_days >= days_needed
        ready = quota_days >= BASE_QUOTA_DAYS * tier
        return {
            'timer_started': start is not None,
            'next_entry': next_entry,
            'next_dex': next_dex,
            'days_needed': days_needed,
            'elapsed_days': elapsed_days,
            'ready': ready,
            'evolvable': True }
    except Exception:
        return 
