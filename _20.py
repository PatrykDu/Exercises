def hamming_distance(v1, v2):
    distance = 0
    if len(v1) != len(v2):
        raise ValueError('Both vectors must be the same length')
    else:
        for x in range(len(v1)):
            if v1[x] != v2[x]:
                distance += 1
    return distance


print(hamming_distance('01101010', '11011011'))
# print(hamming_distance('110', '10100'))
print(hamming_distance('11000', '10100'))
