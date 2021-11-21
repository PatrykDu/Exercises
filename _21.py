def hamming_distance(u, v):
    if len(u) != len(v):
        raise ValueError('Both vectors must be the same length.')
    distance = 0
    for i in range(len(u)):
        if u[i] != v[i]:
            distance += 1
    return distance


def hamming_weight(vector):
    weight = 0
    for i in range(len(vector)):
        if vector[i] == '1':
            weight += 1
    return weight


print(hamming_weight('110001010'))
