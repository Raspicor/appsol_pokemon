# module.PetApp._award_title
# source line 14838
# Recovered from bytecode; default argument values are not shown.

def _award_title(self, title_id, label):
    earned = self.state.setdefault('titles_earned', [])
    for t in earned:
        tid = t.get('id') if isinstance(t, dict) else t
        if not tid == title_id:
            continue
        earned
        return None
    'id'({
        time.strftime: None('%Y-%m-%d %H:%M'),
        label: 'when',
        title_id: 'label' })
    return f'''🏆 새 칭호 획득: {label}'''
