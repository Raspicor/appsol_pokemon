# module.PetApp._grant_legend_ticket
# source line 14626
# Recovered from bytecode; default argument values are not shown.

def _grant_legend_ticket(self, gen):
    key = str(gen)
    tickets = self.state.setdefault('legend_tickets', { })
    tickets[key] = int(tickets.get(key, 0)) + 1
