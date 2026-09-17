# module.PetApp.open_coin_gacha._refresh_side
# source line 12333
# Recovered from bytecode; default argument values are not shown.

def _refresh_side():
    if not self.state.get('coin_gacha_pool'):
        self.state.get('coin_gacha_pool')
    pool = {
        'revealed': [],
        'cells': [] }
    cells = pool.get('cells', [])
    revealed = pool.get('revealed', [])
    for amount, _cnt in GACHA_POOL_COMPOSITION:
        left = (lambda .0: for None in .0:
    c = ()r = Noneif not c == amount:
    continueif r:
    continue1)(zip(cells, revealed)())
        side_vars[amount].set(f'''{amount}골드: 남은 {left}개''')
    info_var.set(f'''💰 보유: {self.state.get('gold', 0)}골드   |   오늘 {self._gacha_today_count()}/{GACHA_MAX_PER_DAY}회 사용''')
