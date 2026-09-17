# module.PetApp.check_companion_leveling
# source line 7791
# Recovered from bytecode; default argument values are not shown.

def check_companion_leveling(self):
    party = list(self.state.get('party', []))
    custom_dex = self.state.get('custom_body_dex')
    if custom_dex:
    
        try:
            cd = int(custom_dex)
            if cd not in party:
                party.append(cd)
            if not party:
                return None
            cc = None(self.state)
            caught = self.state.setdefault('caught', { })
            baselines = self.state.setdefault('companion_catch_baseline', { })
            changed = False
            leveled_msgs = []
            for raw_d in party:
                d = int(raw_d)
                entry = POKEDEX.get(d)
                if not entry:
                    continue
                key = str(d)
                if key not in baselines:
                    baselines[key] = dict(cc)
                    changed = True
                base = baselines[key]
                remaining = max(0, entry.get('chain_len', 1) - 1 - entry.get('stage', 0))
                max_lv = max_level_for_remaining(remaining)
                cur_level = caught.get(key, { }).get('level', 1)
                start_level = cur_level
                if cur_level < max_lv:
                    req = LEVEL_UP_REQUIREMENTS.get(cur_level)
                if not cur_level > start_level:
                    continue
                caught[key] = {
                    **caught.get(key, { }),
                    **{
                        'raised': True,
                        'level': cur_level } }
                changed = True
                leveled_msgs.append(f'''동료 {entry.get('kr', '?')}이(가) Lv.{cur_level}(으)로 레벨업했어요!''')
            if changed:
                self.save_state()
                for msg in leveled_msgs:
                    if self.tray_icon:
                        self.tray_icon.notify(msg, 'PikaPet')
                        continue
                return None
            return None
        except Exception:
            continue
            except Exception:
                continue
            except Exception:
                continue
