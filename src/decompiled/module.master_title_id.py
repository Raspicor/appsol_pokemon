# module.master_title_id
# source line 2010
# Recovered from bytecode; default argument values are not shown.

def master_title_id(mode, gen):
    if mode == 'attack':
        return f'''gen{gen}_master'''
    return f'''{None}_gen{gen}_master'''
