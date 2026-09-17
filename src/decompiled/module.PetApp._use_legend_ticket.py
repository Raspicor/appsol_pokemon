# module.PetApp._use_legend_ticket
# source line 14632
# Recovered from bytecode; default argument values are not shown.

def _use_legend_ticket(self, gen):
    held = int(self.state.get('legend_tickets', { }).get(str(gen), 0))
    if held <= 0:
        return None
    locked_reason = None._shop_gen_locked_reason(gen)
    if locked_reason:
        None('PikaPet', f'''🔒 아직 못 써요 - {locked_reason}.''')
        return None
    None._open_legend_ticket_picker(gen)
