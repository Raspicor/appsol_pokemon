# module.PetApp._open_legend_ticket_picker._pick
# source line 14671
# Recovered from bytecode; default argument values are not shown.

def _pick(dex):
    if state_box['used']:
        return None
    state_box['used'] = None
    for b in buttons:
        b.configure(state = tk.DISABLED)
    self._grant_legend_ticket_pokemon(gen, dex)

    try:
        win.destroy()
        return None
        except Exception:
            continue
    except Exception:
        return None
