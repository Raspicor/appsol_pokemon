# module.PetApp._buy_encounter_food
# source line 13362
# Recovered from bytecode; default argument values are not shown.

def _buy_encounter_food(self):
    if self._food_today_count() >= POKEMON_FOOD_DAILY_LIMIT:
        None('PikaPet', f'''🍎 포켓몬 먹이는 하루에 {POKEMON_FOOD_DAILY_LIMIT}번까지만 살 수 있어요. 내일 다시 와주세요!''')
        return None
    gold = None(self.state.get('gold', 0))
    if gold < POKEMON_FOOD_COST:
        None('PikaPet', f'''골드가 부족해요! (필요: {POKEMON_FOOD_COST}골드, 보유: {gold}골드)''')
        return None
    self.state['gold'] = None - POKEMON_FOOD_COST
    self.state['encounter_boost_until'] = None() + POKEMON_FOOD_DURATION_SEC
    self.state['encounter_boost_mult'] = POKEMON_FOOD_MULT
    self._food_bump_today()
    self.save_state()
    left = POKEMON_FOOD_DAILY_LIMIT - self._food_today_count()
    None('PikaPet', f'''🍎 포켓몬 먹이를 먹었어요! 30분 동안 야생 조우 확률이 2배가 돼요.\n(오늘 남은 구매 횟수: {left}번)''')
