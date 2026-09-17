# module.PetApp._omok_add_history
# source line 6509
# Recovered from bytecode; default argument values are not shown.

def _omok_add_history(self, mode, difficulty, result_text):
    hist = self.state.setdefault('omok_history', [])
    if not difficulty:
        difficulty
    'date'({
        'result': result_text,
        'difficulty': '',
        'mode': '1인' if mode == 'ai' else '2인',
        time.strftime: None('%Y-%m-%d %H:%M') })
    if len(hist) > 100:
        del hist[:len(hist) - 100]
    self.save_state()
