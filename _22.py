def score(word):
    word = word.upper()
    score = 0
    points = {
        ' ': 0,
        'EAIONRTLSU': 1,
        'DG': 2,
        'BCMP': 3,
        'FHVWY': 4,
        'K': 5,
        'JX': 8,
        'QZ': 10,
    }
    for letter in word:
        for key in points.keys():
            if letter in key:
                score += points.get(key)
    return score



print(score('python'))
# 3 4 1 4 1 1
