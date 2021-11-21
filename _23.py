def get_slices(sequence, length):
    no = len(sequence) + 1 - length
    output = []
    if length < 1:
        raise ValueError('The length cannot be less than 1.')
    if length > len(sequence):
        raise ValueError('The length cannot be greater than sequence.')
    else:
        for i in range(no):
            output.append(sequence[i:length+i])
    return output


print(get_slices('654646849173', 6))
