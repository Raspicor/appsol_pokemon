# module.PetApp._show_companion_evolve_info
# source line 7932
# Recovered from bytecode; default argument values are not shown.

def _show_companion_evolve_info(self, d):
    try:
        d = int(d)
        entry = POKEDEX.get(d)
        if not entry:
            return None
        name = None.get('kr', '?')
        lines = [
            f'''{name} (No.{d:03d})''']
        status = self.companion_evolution_status(d)
        if not status.get('evolvable'):
            lines.append(status.get('reason', ''))
        else:
            next_entry = status['next_entry']
            if not status.get('timer_started'):
                lines.append('장착된 뒤로 아직 진화 타이머가 시작되지 않았어요.\n(다음 자동 점검 때 시작돼요)')
            lines.append(f'''다음 진화: {next_entry.get('kr', '?')}''')
            lines.append(f'''진행도: {min(status['elapsed_days'], status['days_needed']):.1f} / {status['days_needed']:.1f}일  (본체와 같은 속도예요)''')
            if status.get('ready'):
                lines.append("✅ 조건을 다 채웠어요! '🧬 진화/레벨 탭'에서 진화시켜보세요.")
        None('진화 조건', '\n'.join(lines))
        return None
    except Exception:
        return None
