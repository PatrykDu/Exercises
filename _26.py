def clean_hashtags(input_file, output_file, length):
    with open(input_file, 'r') as file:
        hashtags = file.read()
        hashtags = hashtags.split()
        output = []
        for hashtag in hashtags:
            if len(hashtag) <= length + 1:
                output.append(hashtag)
        output = set(output)
        output = list(output)
        output.sort()
        with open(output_file, 'w') as clean:
            for item in output:
                clean.write(item + '\n')


clean_hashtags('hashtags.txt', 'clean.txt', 5)
