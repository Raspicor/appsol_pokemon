# module.time_of_day_bucket
# source line 2640
# Recovered from bytecode; default argument values are not shown.

def time_of_day_bucket(t):
    if t is None:
        t = None()
    hour = t.tm_hour
    if  <= 5, hour or 5, hour < 8:
        return 'dawn'
    if  <= 8, hour or 8, hour < 18:
        return 'day'
    if  <= 18, hour or 18, hour < 20:
        return 'dusk'
    return 'night'
    return 'night'
