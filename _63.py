def reduce(function, iterable):
    if len(iterable) == 0:
        return None
    else:
        result = iterable[0]
        for i in iterable[1:]:
            result = function(result, i)
        return result


reduce(lambda x, y: x + y, [1, 2, 3, 4])
