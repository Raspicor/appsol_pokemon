# module.PetApp._check_and_show_gen_certificates
# source line 11218
# Recovered from bytecode; default argument values are not shown.

def _check_and_show_gen_certificates(self):
    gens = newly_completed_gens(self.state)
    if not gens:
        return None
    shown = None.state.setdefault('gen_cert_shown', [])
    for gen in gens:
        self._show_gen_certificate(gen)
        if not gen not in shown:
            continue
        shown.append(gen)
    self.save_state()
