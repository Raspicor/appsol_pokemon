# module.mega_companion_display_kr
# source line 518
# Recovered from bytecode; default argument values are not shown.

def mega_companion_display_kr(dex, entry):
    names = MEGA_NAME_KR.get(int(dex)) if dex is not None else None
    if isinstance(names, dict):
        if not names.get('x'):
            names.get('x')
            if not names.get('y'):
                names.get('y')
                if not entry:
                    entry
        return f'''메가{{ }.get('kr', '?')}'''
    if None(names, str):
        return names
    if not entry:
        entry
    return f'''{{ }.get('kr', '?')}'''
