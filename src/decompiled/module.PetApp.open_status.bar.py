# module.PetApp.open_status.bar
# source line 18435
# Recovered from bytecode; default argument values are not shown.

def bar(label, value):
    f = None(body)
    f.pack(fill = 'x', padx = 14, pady = 4)
    None(f, text = label, width = 10, anchor = 'w').pack(side = 'left')
    pb = None(f, length = 140, maximum = 100, value = max(0, min(100, value)))
    pb.pack(side = 'left', padx = 6)
    None(f, text = f'''{int(value)}%''').pack(side = 'left')
