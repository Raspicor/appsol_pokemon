# module.PetApp.check_companion_evolution
# source line 7740
# Recovered from bytecode; default argument values are not shown.

def check_companion_evolution(self):
    party = list(self.state.get('party', []))
    custom_dex = self.state.get('custom_body_dex')
    targets = list(party)
    if custom_dex:
    
        try:
            targets.append(int(custom_dex))
            if not targets:
                return None
            started_map = None.state.setdefault('companion_evolve_started', { })
            if not isinstance(started_map, dict):
                started_map = { }
                self.state['companion_evolve_started'] = started_map
            changed = False
            for raw_d in targets:
                d = int(raw_d)
                if custom_dex is not None:
                    custom_dex is not None
                is_custom_body = int(custom_dex) == d
                status = self.companion_evolution_status(d)
                if not status.get('evolvable'):
                    continue
                if not status.get('timer_started'):
                    started_map[str(d)] = None()
                    changed = True
                    continue
                if not status.get('ready'):
                    continue
                notif_key = f'''body_swap:{d}''' if is_custom_body else f'''companion:{d}'''
                if not notif_key not in self.state.get('evolve_ready_notified', []):
                    continue
                entry = POKEDEX.get(d, { })
                who = '지금 본체로 나와있는' if is_custom_body else '동료'
                self._notify_evolution_ready(notif_key, f'''{who} {entry.get('kr', '?')}이(가) 진화할 준비가 됐어요!\n우클릭 메뉴의 \'🧬 진화/레벨 탭\'에서 진화시켜보세요.''')
            targets
            if changed:
                self.save_state()
                return None
            return None
        except Exception:
            continue
            except Exception:
                continue
