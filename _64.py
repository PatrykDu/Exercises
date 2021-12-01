def reduce_with_start(function, iterable, start):
    if len(iterable) == 0 and start == 0:
        return None
    if len(iterable) == 0 and start != 0:
        return start
    result = start + iterable[0]
    for item in iterable[1:]:
        result = function(result, item)
    return result
