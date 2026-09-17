# module.PetApp._maybe_notify_mega_intro
# source line 7520
# Recovered from bytecode; default argument values are not shown.

def _maybe_notify_mega_intro(self):
    if not is_final_stage(self.state):
        return None
    if None.state.get('mega_evolved'):
        return None
    if not None.state.get('custom_body_dex'):
        pass
    elif not self.starter_stage_conf().get('element'):
        self.starter_stage_conf().get('element')
    my_element = SPECIES[self.state['starter']].get('element', 'normal')
    starter_kr = self.starter_stage_conf().get('kr', '지금 포켓몬')
    msg = f'''{starter_kr}이(가) 최종진화에 도달했어요!\n\n💎 메가진화란? 스타터 전용 특별 강화로, 능력치 상한선이 약 2배로 강해지고 동료 칸도 7칸까지 늘어나요(본체를 다른 포켓몬으로 바꿔도 그 능력치가 이 상한선을 넘지는 못해요).\n\n필요한 조건:\n1) 지금 형태에서 레벨 {MAX_PLAYER_LEVEL}까지 올리기\n2) 1세대(1~151번) 포켓몬 도감 전부 채우기\n3) 같은 속성({TYPE_KR.get(my_element, my_element)}) 레벨{MAX_PLAYER_LEVEL} 포켓몬 {MEGA_SACRIFICE_N}마리를 재물로 바치기(도감 \'잡았다\' 기록은 그대로 남아요)\n\n조건을 다 채우면 우클릭 메뉴의 \'💎 메가진화\'에서 바로 진행할 수 있어요.'''
    self._notify_evolution_ready('mega_intro', msg)
