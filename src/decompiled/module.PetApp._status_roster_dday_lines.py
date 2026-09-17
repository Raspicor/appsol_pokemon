# module.PetApp._status_roster_dday_lines
# source line 8057
# Recovered from bytecode; default argument values are not shown.

def _status_roster_dday_lines(self):
    lines = [
        self._status_body_dday_line()]
    for d in self.state.get('party', []):
        ln = self._status_companion_dday_line(d)
        if not ln:
            continue
        lines.append(ln)
    return lines
