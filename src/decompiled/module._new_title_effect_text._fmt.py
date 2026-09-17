# module._new_title_effect_text._fmt
# source line 2435
# Recovered from bytecode; default argument values are not shown.

def _fmt(d):
    parts = []
    for None in d.items():
        k = ()
        v = None
        if not v:
            continue
        if k in flat_labels:
            parts.append(f'''{flat_labels[k]}+{v:.0f}''')
            continue
        if k == 'mirror_pct':
            parts.append(f'''{v:.0f}% 확률로 상대방 공격 미러링(반사)''')
            continue
        if not k in labels:
            continue
    if parts:
        return ', '.join(parts)
