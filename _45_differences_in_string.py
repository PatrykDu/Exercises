def lev(a, b):
    if b == 0:
        return len(a)

    if a == 0:
        return len(b)

    if len(a) > len(b):
        score = len(a) - len(b)
        temp = len(a) - len(b)
        i = 0
        while i < len(a) - temp:
            if a[i] != b[i]:
                score += 1
            i += 1
        return score

    if len(b) > len(a):
        score = len(b) - len(a)
        temp = len(b) - len(a)
        i = 0
        while i < len(b) - temp:
            if b[i] != a[i]:
                score += 1
            i += 1
        return score

    if len(a) == len(b):
        score = 0
        i = 0
        while i < len(a):
            if a[i] != b[i]:
                score += 1
            i += 1
        return score


print(lev('c++', 'c'))
