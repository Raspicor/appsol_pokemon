# module.time_of_day_type_mult
# source line 2666
# Recovered from bytecode; default argument values are not shown.

def time_of_day_type_mult(entry, bucket):
    if bucket is None:
        bucket = time_of_day_bucket()
    table = TIME_TYPE_WEIGHT.get(bucket, { })
    if not table:
        return 1
    mult = None
    for t in pokedex_types(entry):
        mult = max(mult, table.get(t, 1))
    return mult
