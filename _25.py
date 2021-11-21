def clean_hashtags():
    file = open('hashtags.txt', 'r').read()
    hashtags = file.split()
    output = []
    for hashtag in hashtags:
        if len(hashtag) <= 5:
            output.append(hashtag)
    output = set(output)
    output = list(output)
    output.sort()
    return output


print(clean_hashtags())
